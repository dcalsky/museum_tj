from django.contrib import admin

from .models import Article, Part


class PartAdmin(admin.ModelAdmin):
    list_display = ['name', 'title']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'desc', 'part', 'create_time']


admin.site.register(Article, ArticleAdmin)

admin.site.register(Part, PartAdmin)