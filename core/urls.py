from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<keywords>\w+)', views.search)
]