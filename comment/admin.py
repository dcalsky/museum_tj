# coding=utf-8

from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('审核通过', {'fields': ['verify']}),
        ('申请时间', {'fields': ['create_time']}),
        ('基本信息', {'fields': ['title', 'name', 'email', 'content']})
    ]
    list_display = ['title', 'name', 'email', 'create_time', 'verify']

admin.site.register(Comment, CommentAdmin)
