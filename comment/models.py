from django.db import models


class Comment(models.Model):
    title = models.CharField(max_length=40)
    name = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
    content = models.TextField()
    create_time = models.DateTimeField()

