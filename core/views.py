# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse

from vector.models import Article, Part


def home(request):
    news_part = Part.objects.get(name='news')
    #exhibitions_part = Part.objects.get(name='网上巡展')
    #slider_part = Part.objects.get(name='轮播图')

    #sliders = slider_part.article_set.order_by('create_time')[:5]
    news = news_part.article_set.order_by('create_time')[:5]
    #exhibitions = exhibitions_part.article_set.order_by('create_time')[:5]
    return render(request, 'core/core.html', {
        'news': news
    })


def part(request):
    return HttpResponse("part")
