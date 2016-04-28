from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField

class Part(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=20)


class Article(models.Model):
    def __str__(self):
        return self.title

    part = models.ForeignKey(Part)
    title = models.CharField(max_length=20)
    content = RichTextField()
    desc = models.CharField(max_length=150)
    thumbnail = models.TextField()
    create_time = models.DateTimeField('created time')
    page_view = models.IntegerField(default=0)


