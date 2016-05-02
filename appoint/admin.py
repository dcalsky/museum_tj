from django.contrib import admin
from .models import Appoint


class AppointAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact', 'time', 'finished']

admin.site.register(Appoint, AppointAdmin)
