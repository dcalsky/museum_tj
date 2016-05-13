from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST
from django.db.models import Q

from vector.models import Article


@require_GET
def search(request):
    return render(request, 'search/main.html')


@require_POST
def handle_search(request):
    keywords = request.GET.get('keywords').strip()
    results = Article.objects.filter(Q(title__contains=keywords) | Q(content__contains=keywords))
    return render(request, 'search/detail.html', {
        'articles': results
    })
