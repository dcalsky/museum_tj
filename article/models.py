from __future__ import unicode_literals
from django.db import models


class Part(models.Model):
    name = models.CharField(max_length=20)


class Article(models.Model):
    part = models.ForeignKey(Part)
    title = models.CharField(max_length=20)
    content = models.TextField()
    desc = models.CharField(max_length=150)
    thumbnail = models.TextField()
    create_time = models.DateTimeField('created time')
    page_view = models.IntegerField(default=0)

    def get_part_name(self):
        return self.part.name
