from django.shortcuts import render
from django.http import HttpResponse

from museum_tj.article.models import Article

def home(request):
    news = Article.get_article()
    return render(request, 'core/home.html', {
        'news': news
    })
