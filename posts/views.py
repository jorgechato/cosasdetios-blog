from django.shortcuts import render
from django.shortcuts import get_object_or_404
from datetime import date
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from django.core.paginator import Paginator


from .models import Post
from .models import Category


class PostListView(ListView):
    queryset = Post.objects.filter(public=True, published_at__lte=date.today())


class PostDetailView(DetailView):
    model = Post


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    post_list = Post.objects.filter(categories_id=category, public=True, published_at__lte=date.today())
    template = 'category_detail.html'

    page = request.GET.get('page', 1)

    paginator = Paginator(post_list, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, template, locals())
