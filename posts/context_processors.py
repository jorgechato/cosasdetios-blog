from .models import Category
from django.core.urlresolvers import reverse


def nav(request):
    list_cat = Category.objects.order_by('order')
    menu = {
            'categories': list_cat,
            }

    for category in menu['categories']:
        if request.path is category:
            print category
            # category['active'] = True

    return menu
