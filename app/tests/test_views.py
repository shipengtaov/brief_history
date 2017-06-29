# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import re
from django.test import TestCase
from django.shortcuts import reverse
from ..models import Page, Domain, PageDomain


class ViewsTest(TestCase):
    def test_home_response_ok(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')

    def test_home_has_all_domains(self):
        domain1 = Domain(name='测试领域', keywords='关键字1|关键字2')
        domain1.save()
        domain2 = Domain(name='测试领域2', keywords='关键字1|关键字3')
        domain2.save()
        resp = self.client.get(reverse('home'))
        resp.text = resp.content.decode('utf-8')
        self.assertIn(domain1.name, resp.text)
        self.assertIn(domain1.get_absolute_url(), resp.text)
        self.assertIn(domain2.name, resp.text)
        self.assertIn(domain2.get_absolute_url(), resp.text)

    def test_home_has_pages(self):
        page1 = Page(title='人物1', url='https://test1.org',
                     birth_date='2017-06-30', has_birth_date=True)
        page1.save()
        page2 = Page(title='人物2', url='https://test2.org',
                     birth_date='2017-07-01', has_birth_date=True)
        page2.save()
        resp = self.client.get(reverse('home'))
        resp.text = resp.content.decode('utf-8')
        self.assertIn(page1.title, resp.text)
        self.assertIn(page1.url, resp.text)
        self.assertIn(page1.birth_date, resp.text)
        self.assertIn(page2.title, resp.text)
        self.assertIn(page2.url, resp.text)
        self.assertIn(page2.birth_date, resp.text)

    def test_pages_sorted_by_birth_date(self):
        pass

    def test_domain_page_ok(self):
        domain = Domain(name='测试领域', keywords='关键字1|关键字2')
        domain.save()
        resp = self.client.get(reverse('domain', kwargs=dict(domain_id=domain.id)))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')

    def test_domain_page_has_title(self):
        domain = Domain(name='测试领域', keywords='关键字1|关键字2')
        domain.save()
        resp = self.client.get(reverse('domain', kwargs=dict(domain_id=domain.id)))
        resp.text = resp.content.decode('utf-8')
        self.assertRegexpMatches(resp.text, r'<title>.*?{}.*?</title>'.format(domain.name))

    def test_domain_page_has_all_domains(self):
        domain = Domain(name='测试领域', keywords='关键字1|关键字2')
        domain.save()
        resp = self.client.get(reverse('domain', kwargs=dict(domain_id=domain.id)))
        resp.text = resp.content.decode('utf-8')
        self.assertIn(domain.get_absolute_url(), resp.text)
        self.assertRegexpMatches(resp.text.replace('\n', ''), r'<body>.*?{}.*?</body>'.format(domain.name))

    def test_domain_page_current_domain(self):
        pass
