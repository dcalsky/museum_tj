from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.get_part),
    url(r'^(?P<article_id>\d+$)', views.get_article)
]