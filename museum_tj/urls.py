
from django.conf.urls import url, include
from django.contrib import admin

from vector import views as view_vector
from core import views as view_home
from appoint import views as view_appoint
from comment import views as view_comment
from search import views as view_search


urlpatterns = [
    url(r'^museum/$', view_home.home, name='home'),
    url(r'admin/', admin.site.urls),
    url(r'part/(?P<part_name>\w+)/', include('vector.urls'), name='part'),
    url(r'^search$', view_search.search, name='search'),
    url(r'^appoint$', view_appoint.apply_appoint, name='appoint'),
    url(r'comment', include('comment.urls')),
    url(r'^summernote/', include('django_summernote.urls')),
]
