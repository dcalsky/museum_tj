from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.decorators.http import require_POST, require_GET
from django_ajax.decorators import ajax
from .models import Comment


def get_comments(request):
    return render(request, 'comment/comments.html')


@ajax
def next_comment(request):
    comments = Comment.objects.filter(verify=True)
    paginator = Paginator(comments, 4)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        comments = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        comments = paginator.page(paginator.num_pages)
    return {
        'comments': comments
    }


@require_POST
def post_comment(request):
    comment = Comment(
        title=request.POST.get('title'),
        content=request.POST.get('content'),
    )
    comment.save()
    return HttpResponse("评论成功")
