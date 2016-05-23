from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST

from .models import Comment


def get_comments(request):
    comments = Comment.objects.filter(verify=True)
    return render(request, 'comment/comments.html', {
        comments: comments
    })


@require_POST
def post_comment(request):
    comment = Comment(
        title=request.POST.get('title'),
        content=request.POST.get('content'),
    )
    comment.save()
    return HttpResponse("评论成功")
