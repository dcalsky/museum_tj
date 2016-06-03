from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^/$', views.get_comments),
    url(r'post$', views.post_comment, name='post'),
    url(r'get$', views.next_comment, name='get'),
]
