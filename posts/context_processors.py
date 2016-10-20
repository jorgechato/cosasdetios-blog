from .models import Category


def nav(request):
    list_cat = Category.objects.order_by('order')
    menu = {
            'categories': list_cat,
            }

    for category in menu['categories']:
        if request.path == category.get_absolute_url():
            category.active = True

    return menu
