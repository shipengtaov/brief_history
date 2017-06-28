# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import models


class Page(models.Model):
    """对应于维基百科页面
    """
    title = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=500, null=True)
    birth_date = models.CharField(max_length=10, default='0000-00-00')
    death_data = models.CharField(max_length=10, default='0000-00-00')
    text = models.TextField()

    def __str__(self):
        return '<Page {}>'.format(self.title)

    def get_absolute_url(self):
        pass

    class Meta:
        pass


class Domain(models.Model):
    """领域
    """
    name = models.CharField(verbose_name='领域名', max_length=200)
    keywords = models.CharField(verbose_name='包含哪些关键字', max_length=500, null=True)

    def __str__(self):
        return '<Domain {}>'.format(self.name)

    def get_absolute_url(self):
        pass


class PageDomain(models.Model):
    domain = models.ForeignKey(Domain)
    page = models.ForeignKey(Page)
