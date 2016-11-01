from django.conf.urls import url

from views import PostListView
from views import PostDetailView
from views import category_detail

app_name = 'articles'

urlpatterns = [
        # url(r'^$', PostListView.as_view(), name='list'),
        url(r'^(?P<categories_id>[-\w]+)/(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name='detail'),
        url(r'^(?P<slug>[-\w]+)/$', category_detail, name='category'),
        ]
