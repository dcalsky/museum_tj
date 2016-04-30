from django.db import models


class Part(models.Model):
    title = models.CharField(max_length=20)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Article(models.Model):
    part = models.ForeignKey(Part)
    title = models.CharField(max_length=40)
    desc = models.CharField(max_length=150)
    create_time = models.DateTimeField()
    thumbnail = models.ImageField()
    secret = models.BooleanField(default=False)
    page_view = models.IntegerField(default=0)

    class Meta:
        ordering = ['create_time']

    def __str__(self):
        return self.title