# coding=utf-8
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from json import dumps
from django.core.serializers import serialize

from vector.models import Article, Part
from appoint.forms import AppointForm


def home(request):
    news_part = Part.objects.get(name='news')
    exhibitions_part = Part.objects.get(name='exhibition')
    slider_part = Part.objects.get(name='slider')

    sliders = slider_part.article_set.order_by('create_time')[:5] or []
    news = news_part.article_set.order_by('create_time')[:5] or []
    exhibitions = exhibitions_part.article_set.order_by('create_time')[:4] or []
    # appoint_form = AppointForm()
    return render(request, 'core/core.html', {
        'news': news,
        'exhibitions': exhibitions,
        'sliders': sliders
        # 'appoint_form': appoint_form
    })


def load_more(request, page=1):
    page = int(page)
    news_part = Part.objects.get(name='news')
    # exhibitions_part = Part.objects.get(name='exhibition')
    news_total = news_part.article_set.order_by('create_time')[page * 5: (page + 1) * 5] or []
    news_json = serialize("json", news_total)
    # exhibitions = exhibitions_part.article_set.order_by('create_time')[page * 4: (page + 1) * 4] or []
    # news_json = map(lambda news: {
    #     "id": news.get('id'),
    #     "title": news.get('title'),
    #     "thumbnail": {
    #         "url": news.get('thumbnail').url
    #     }
    # }, news_total)
    return HttpResponse(news_json, content_type="application/json")
