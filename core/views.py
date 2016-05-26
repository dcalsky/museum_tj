# coding=utf-8
from django.shortcuts import render

from vector.models import Article, Part
from appoint.forms import AppointForm


def home(request):
    news_part = Part.objects.get(name='news')
    exhibitions_part = Part.objects.get(name='exhibition')
    slider_part = Part.objects.get(name='slider')

    sliders = slider_part.article_set.order_by('create_time')[:5] or []
    news = news_part.article_set.order_by('create_time')[:5] or []
    exhibitions = exhibitions_part.article_set.order_by('create_time')[:4] or []
    appoint_form = AppointForm()
    return render(request, 'core/core.html', {
        'news': news,
        'exhibitions': exhibitions,
        'sliders': sliders,
        'appoint_form': appoint_form
    })
