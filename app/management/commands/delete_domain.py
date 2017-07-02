# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.management.base import BaseCommand, CommandError
from django.utils.encoding import force_text

from app.models import Page, Domain, PageDomain


class Command(BaseCommand):
    help = 'Delete one specific domain by name - Brief History'

    def add_arguments(self, parser):
        parser.add_argument('-n', '--name', required=True, help='domain name')

    def handle(self, *args, **options):
        name = force_text(options['name'])
        try:
            domain = Domain.objects.get(name=name)
        except Domain.DoesNotExist:
            raise CommandError('domain does not exist: {}'.format(name))
        for r in domain.pagedomain_set.all():
            r.delete()
            if not PageDomain.objects.filter(page_id=r.page.id).exclude(domain=domain):
                print('deleting page: {}'.format(r.page.title))
                r.page.delete()
        print('deleting domain: {}'.format(domain.name))
        domain.delete()
