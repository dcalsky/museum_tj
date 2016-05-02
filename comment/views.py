from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

from .models import Comment


def _get_comments(request):
    comments = Comment.objects.filter(verify=True)
    render(request, 'comment/comments.html', {
        comments: comments
    })


@require_POST
def post_comment(request):
    comment = Comment(
        title=request.POST('title'),
        name=request.POST('name'),
        email=request.POST('email'),
        phone=request.POST('phone'),
        content=request.POST('content'),
    )
    comment.save()
