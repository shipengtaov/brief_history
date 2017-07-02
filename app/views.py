# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Page, Domain


def home(request):
    try:
        page = int(request.GET.get('page', 1))
        assert page > 0
    except (ValueError, AssertionError):
        page = 1
    try:
        per_page = int(request.GET.get('per_page', 50))
        assert 0 < per_page <= 100
    except (ValueError, AssertionError):
        per_page = 50
    pages = Paginator(Page.objects.all(), per_page).page(page)
    context = dict(
        title='Brief History',
        pages=pages,
        domains=Domain.objects.all(),
    )
    return render(request, 'index.html', context)


def domain(request, domain_id):
    try:
        page = int(request.GET.get('page', 1))
        assert page > 0
    except (ValueError, AssertionError):
        page = 1
    try:
        per_page = int(request.GET.get('per_page', 50))
        assert 0 < per_page <= 100
    except (ValueError, AssertionError):
        per_page = 50

    domain = get_object_or_404(Domain, pk=domain_id)
    pages = Page.objects.filter(pagedomain__domain=domain)
    p = Paginator(pages, per_page)
    pages = p.page(page)
    context = dict(
        title='{} - Brief History'.format(domain.name),
        current_domain=domain,
        domains=Domain.objects.all(),
        pages=pages,
    )
    return render(request, 'index.html', context)
