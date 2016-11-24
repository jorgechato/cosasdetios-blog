from django.utils import timezone

from posts.models import Category
from posts.models import SideBar
from posts.models import Post
from podcast.models import Episode


def nav(request):
    list_cat = Category.objects.order_by('order')
    menu = {
            'categories': list_cat,
            }

    for category in menu['categories']:
        if request.path == category.get_absolute_url():
            category.active = True

    return menu


def sidebar(request):
    list_items = SideBar.objects.filter().order_by('order')
    posts = Post.objects.filter(public=True, published_at__lte=timezone.now()).order_by('?')[:5]
    podcast = Episode.objects.filter(pub_date__lte=timezone.now()).order_by('?')[:3]
    items = {
            'items': list_items,
            'posts': posts,
            'podcast': podcast,
            }

    return items


def footer(request):
    podcast = Episode.objects.filter(pub_date__lte=timezone.now()).order_by('?')[:5]
    posts = Post.objects.filter(public=True, published_at__lte=timezone.now()).order_by('?')[:5]
    items = {
            'posts': posts,
            'podcast': podcast,
            }

    return items
