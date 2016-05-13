from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Article, Part


class PartAdmin(admin.ModelAdmin):
    list_display = ['name', 'title']


class ArticleAdmin(SummernoteModelAdmin):
    list_display = ['title', 'desc', 'part', 'create_time']


admin.site.register(Article, ArticleAdmin)

admin.site.register(Part, PartAdmin)