# coding=utf-8
from django.db import models


class Appoint(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    time = models.CharField(max_length=35)
    phone = models.CharField(max_length=20)
    note = models.TextField(blank=True)
    finished = models.BooleanField(default=False)

    class Meta:
        ordering = ['finished']

    def __str__(self):
        return self.name + ' 的预约'
