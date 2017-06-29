# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import models
from django.shortcuts import reverse


class Page(models.Model):
    """对应于维基百科页面
    """
    UNKNOWN_DATE = '0000-00-00'
    title = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=500, null=True)
    birth_date = models.CharField(max_length=10, default=UNKNOWN_DATE)
    death_date = models.CharField(max_length=10, default=UNKNOWN_DATE)
    has_birth_date = models.BooleanField(default=False)
    text = models.TextField()

    def __str__(self):
        return '<Page {}>'.format(self.title)

    def birth_death_date(self):
        if self.birth_date == self.UNKNOWN_DATE and self.death_date == self.UNKNOWN_DATE:
            return '未知'
        if self.birth_date == self.UNKNOWN_DATE:
            return '未知~{}'.format(self.death_date)
        if self.death_date == self.UNKNOWN_DATE:
            return '{}~'.format(self.birth_date)
        return '{}~{}'.format(self.birth_date, self.death_date)


class Domain(models.Model):
    """领域
    """
    name = models.CharField(verbose_name='领域名', max_length=200)
    keywords = models.CharField(verbose_name='包含哪些关键字', max_length=500, null=True)

    def __str__(self):
        return '<Domain {}>'.format(self.name)

    def get_absolute_url(self):
        return reverse('domain', kwargs=dict(domain_id=self.pk))


class PageDomain(models.Model):
    domain = models.ForeignKey(Domain)
    page = models.ForeignKey(Page)
