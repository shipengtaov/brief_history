# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Page, Domain


def home(request):
    pages = Page.objects.all()
    context = dict(
        title='Brief History',
        pages=pages,
        domains=Domain.objects.all(),
    )
    return render(request, 'index.html', context)


def domain(request, domain_id):
    domain = get_object_or_404(Domain, pk=domain_id)
    pages = Page.objects.filter(pagedomain__domain=domain)
    context = dict(
        title='{} - Brief History'.format(domain.name),
        domain=domain,
        domains=Domain.objects.all(),
        pages=pages,
    )
    return render(request, 'index.html', context)
