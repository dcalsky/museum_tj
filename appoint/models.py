# coding=utf-8
from django.db import models


class Appoint(models.Model):
    name = models.CharField(max_length=40, blank=True)
    email = models.EmailField(blank=True)
    time = models.CharField(max_length=40, blank=True)
    phone = models.CharField(max_length=40, blank=True)
    note = models.TextField(blank=True)
    amount = models.CharField(max_length=40, blank=True)
    finished = models.BooleanField(default=False)

    class Meta:
        ordering = ['finished']

    def __str__(self):
        return self.name + ' 的预约'
