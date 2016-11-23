from django.contrib.sitemaps import Sitemap
from django.utils import timezone


from posts.models import Post
from posts.models import Category
from podcast.models import Episode


class PodcastSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Episode.objects.filter(pub_date__lte=timezone.today())

    def lastmod(self, obj):
        return obj.pub_date


class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return obj.published_at


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.filter(public=True, published_at__lte=timezone.today())

    def lastmod(self, obj):
        return obj.published_at
