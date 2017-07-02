# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.test import TestCase
from ..models import Domain


class DomainTest(TestCase):
    def test_keywords(self):
        domain = Domain('领域1', keywords='关键字1|关键字2|关键字3')
        self.assertEqual(['关键字1', '关键字2', '关键字3'], domain.get_keywords())
