# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

from vector.models import Article, Part
from comment.views import _get_comments


def home(request):
    news_part = Part.objects.get(name='news')
    exhibitions_part = Part.objects.get(name='exhibition')
    slider_part = Part.objects.get(name='slider')

    sliders = slider_part.article_set.order_by('create_time')[:5] or []
    news = news_part.article_set.order_by('create_time')[:5] or []
    exhibitions = exhibitions_part.article_set.order_by('create_time')[:3] or []
    comments = _get_comments(request) or []
    return render(request, 'core/core.html', {
        'news': news,
        'comments': comments,
        'exhibitions': exhibitions,
        'sliders': sliders
    })


def search(request):
    keywords = request.GET.get('keywords').strip()
    results = Article.objects.filter(Q(title__contains=keywords) | Q(content__contains=keywords))
    return render(request, 'search/detail.html', {
        'results': results
    })

