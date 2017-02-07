from django import forms
from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from ckeditor.widgets import CKEditorWidget

from .models import Post
from .models import Category
from .models import SideBar


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = "__all__"


class PostAdmin(ImportExportActionModelAdmin):
    form = PostAdminForm

    list_display = ('cover_image', 'title', 'published_at', 'public', 'slug')
    list_filter = ('published_at', 'public')
    list_display_links = ('cover_image', 'title',)
    search_fields = ('title',)
    ordering = ('-published_at',)

    def cover_image(self, obj):
        tag = '<img src="https://placeholdit.imgix.net/~text?txtsize=23&bg=000000&txtclr=D3367E&txt=%s&w=200&h=100">' % obj.title
        if obj.thumbnail:
            tag = '<img src="https://placeholdit.imgix.net/~text?txtsize=23&bg=D3367E&txtclr=000000&txt=%s&w=200&h=100">' % obj.title
        return tag

    cover_image.allow_tags = True


class CategoryAdmin(ImportExportActionModelAdmin):
    list_display = ('title', 'order', 'keywords', 'description')
    list_display_links = ('title',)
    search_fields = ('title',)
    ordering = ('-order',)


class SideBarAdmin(ImportExportActionModelAdmin):
    list_display = ('content', 'title', 'order', 'cover_content',)
    list_display_links = ('content', 'title')
    list_filter = ('title', 'categories_id')
    search_fields = ('title', 'categories_id')
    filter_horizontal = ('categories_id',)
    ordering = ('-order',)

    def cover_content(self, obj):
        return obj.content

    cover_content.allow_tags = True

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SideBar, SideBarAdmin)
