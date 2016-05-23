from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.get_comments),
    url(r'^comment$', views.post_comment, name='comment')
]