from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from vector.models import Article, Part


def get_article(request, part_name, article_id):
    article = Article.objects.filter(id=article_id)
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
    return render(request, 'vector/detail.html', {
        'articles': articles
    })


def get_part(request, part_name):
    part = Part.objects.get(name=part_name)
    return _get_articles(request, part)
