from datetime import date
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import TemplateView

from .models import Post
from .models import Category
from .models import SideBar


class BaseView(TemplateView):
    pass


class PostListView(ListView):
    queryset = Post.objects.filter(public=True, published_at__lte=date.today())
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post


class CategoryDetailView(DetailView):
    model = Category
