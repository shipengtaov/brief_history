# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from os import path
from multiprocessing import Process

from django.core.management.base import BaseCommand, CommandError
from django.utils.encoding import force_text
from lxml import etree

from app.models import Page, Domain, PageDomain
from app.utils import is_wiki_about_person, get_birth_death_date


class Command(BaseCommand):
    help = 'Import your downloaded wikipedia - Brief History'
    requires_migration_checks = True

    def add_arguments(self, parser):
        parser.add_argument('-f', '--file', required=True, help='your downloaded wikipedia file')
        parser.add_argument('-d', '--domain', required=True, help='which domain')
        parser.add_argument('-k', '--keywords', nargs='+', required=True, help='keywords of the domain')
        parser.add_argument('-l', '--lang', required=True, help="what's your wikipedia's language. example: zh|en")
        parser.add_argument('-M', '--max', type=int, help='max person counte')

    def handle(self, *args, **options):
        file = options['file']
        domain = force_text(options['domain'])
        keywords = [force_text(i).lower() for i in options['keywords']]
        lang = options['lang']
        max_count = options['max']

        file = path.expanduser(file)
        # relative path
        if not file.startswith('/'):
            file = path.join(path.dirname(path.abspath(__file__)), file)
        if not path.exists(file):
            raise CommandError('file does not exist: {}'.format(file))

        domain, created = Domain.objects.get_or_create(name=domain)
        domain.keywords = '|'.join(keywords)
        domain.save()

        parsed = etree.iterparse(file)
        counter = 0
        for event, element in parsed:
            if not element.tag.endswith('page'):
                continue
            title = element.xpath('./*[contains(name(), "title")]')[0].text
            if ':' in title:
                continue
            text = element.xpath('.//*[contains(name(), "text")]')[0].text
            if not text:
                continue

            if not any([i in text for i in keywords]):
                continue
            if not is_wiki_about_person(text):
                continue

            url = 'https://{}.wikipedia.org/wiki/{}'.format(lang, title)
            birth_date, death_date = get_birth_death_date(text)

            # import ipdb
            # if not birth_date:
            #     print(title)
            #     ipdb.set_trace()
            page, created = Page.objects.get_or_create(title=title)
            page.url = url
            if birth_date:
                page.birth_date = birth_date.isoformat()
                page.has_birth_date = True
            if death_date:
                page.death_date = death_date.isoformat()
            page.save()

            relation, created = PageDomain.objects.get_or_create(domain=domain, page=page)
            relation.save()

            counter += 1
            self.stdout.write('{}: added {}'.format(counter, title))
            if max_count and counter >= max_count:
                break

        self.stdout.write('done. total: {}'.format(counter))
