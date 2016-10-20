from django.shortcuts import render
from django.shortcuts import get_object_or_404
from datetime import date
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import TemplateView

from .models import Post
from .models import Category


class PostListView(ListView):
    queryset = Post.objects.filter(public=True, published_at__lte=date.today())


class PostDetailView(DetailView):
    model = Post


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(categories_id=category, public=True, published_at__lte=date.today())
    template = 'category_detail.html'

    return render(request, template, locals())
