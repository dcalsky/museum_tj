from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^(?P<page>\d+$)', views.load_more)
]