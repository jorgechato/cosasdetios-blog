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
        tag = '<img src="https://placeholdit.imgix.net/~text?txtsize=23&bg=E8117f&txtclr=ffffff&txt=%s&w=200&h=100">' % obj.title
        if obj.thumbnail:
            url = obj.thumbnail.url
            tag = '<img src="%s" style="width:200px;">' % url
        return tag

    cover_image.allow_tags = True


class CategoryAdmin(ImportExportActionModelAdmin):
    list_display = ('title', 'order', 'keywords', 'description')
    list_display_links = ('title',)
    search_fields = ('title',)
    ordering = ('-order',)


class SideBarAdmin(ImportExportActionModelAdmin):
    list_display = ('title', 'order', 'cover_content',)
    list_display_links = ('title',)
    search_fields = ('title',)
    ordering = ('-order',)

    def cover_content(self, obj):
        return obj.content

    cover_content.allow_tags = True

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SideBar, SideBarAdmin)