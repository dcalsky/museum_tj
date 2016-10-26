# coding=utf-8

from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from json import dumps
from django.core.serializers import serialize
from .models import Article, Part


def home(request):
    news = Article.objects.filter(part__name='news').order_by('create_time')[:5] or []
    sliders = Article.objects.filter(part__name='sliders').order_by('create_time')[:5] or []
    exhibitions = Article.objects.filter(part__name='exhibitions').order_by('create_time')[:4] or []

    # news_part = Part.objects.get(name='news') or None
    # exhibitions_part = Part.objects.get(name='exhibition') or []
    # slider_part = Part.objects.get(name='slider') or []
    #
    # sliders = slider_part.article_set.order_by('create_time')[:5] or []
    # news = news_part.article_set.order_by('create_time')[:5] or []
    # exhibitions = exhibitions_part.article_set.order_by('create_time')[:4] or []
    return render(request, 'core/home.html', {
        'news': news,
        'exhibitions': exhibitions,
        'sliders': sliders
        # 'appoint_form': appoint_form
    })


def load_more(request, page=1):
    page = int(page)
    exhibitions_part = Part.objects.get(name='exhibition')
    exhibitions_total = exhibitions_part.article_set.order_by('create_time')[page * 4: (page + 1) * 4] or []
    exhibitions_json = serialize("json", exhibitions_total)
    return HttpResponse(exhibitions_json, content_type="application/json")
