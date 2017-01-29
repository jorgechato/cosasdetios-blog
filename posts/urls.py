from django.conf.urls import url

from views import PostDetailView
from views import ThoughtsListView
from views import PostListView

app_name = 'articles'

urlpatterns = [
        url(r'^reflexiones$', ThoughtsListView.as_view(), name="thoughts"),
        url(r'^(?P<categories_id>[-\w]+)/(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name='detail'),
        url(r'^(?P<slug>[-\w]+)/$', PostListView.as_view(), name='category'),
        ]
