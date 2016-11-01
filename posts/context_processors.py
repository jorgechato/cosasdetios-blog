from datetime import date

from .models import Category
from .models import SideBar
from .models import Post


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
    posts = Post.objects.filter(public=True, published_at__lte=date.today()).order_by('?')[:5]
    items = {
            'items': list_items,
            'posts': posts,
            }

    return items


def footer(request):
    return {}
