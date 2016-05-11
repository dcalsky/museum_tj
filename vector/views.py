from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist

from vector.models import Article, Part


def get_article(request, part_name, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except:
        article = None
    return render(request, 'vector/detail.html', {
        'article': article
    })


def _get_articles(request, part):
    articles = Article.objects.filter(part=part)
    paginator = Paginator(articles, 10)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request, 'vector/part.html', {
        'articles': articles,
        'part': part,
    })


def get_part(request, part_name):
    try:
        part = Part.objects.get(name=part_name)
    except ObjectDoesNotExist:
        part = None
    return _get_articles(request, part)
