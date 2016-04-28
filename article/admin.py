# coding=utf-8
from django.contrib import admin

from .models import Article, Part


class PartAdmin(admin.ModelAdmin):
    list_display = ['name']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'part']

admin.site.register(Article, ArticleAdmin)

admin.site.register(Part, PartAdmin)