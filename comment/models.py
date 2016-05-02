from django.db import models
from datetime import datetime


class Comment(models.Model):
    title = models.CharField(max_length=40)
    name = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
    content = models.TextField()
    create_time = models.DateTimeField(default=datetime.today())
    verify = models.BooleanField(default=False)

    class Meta:
        ordering = ['create_time']

    def __str__(self):
        return self.title
