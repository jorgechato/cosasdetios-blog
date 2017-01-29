from local_settings import USE_S3
from django.conf import settings
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.conf.urls import handler400, handler403, handler404, handler500
from django.views.generic import TemplateView
from rest_framework import routers

from .sitemap import PostSitemap
from .sitemap import CategorySitemap
from .sitemap import PodcastSitemap
from . import views

sitemaps = {
        'podcast': PodcastSitemap,
        'post': PostSitemap,
        'categoria': CategorySitemap,
        }

router = routers.DefaultRouter()
router.register(r'shows', views.ShowViewSet)
router.register(r'episodes', views.EpisodeViewSet)
router.register(r'enclosures', views.EnclosureViewSet)

urlpatterns = [
        url(r'^cookies/', TemplateView.as_view(template_name='cookies-law.html')),
        url(r'^admin/', admin.site.urls),
        url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
        url(r'^api/v1/', include(router.urls, namespace='api')),
        url(r'^', include('podcast.urls'), name="home"),
        url(r'^historias/', include('posts.urls'), name="articles"),
        url(r'^robots\.txt', include('robots.urls')),
        url(r'^sitemap-(?P<section>.+)\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
        url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.index'),
        ]

if not USE_S3:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler400 = 'cosasdetios.views.bad_request'
handler403 = 'cosasdetios.views.permission_denied'
handler404 = 'cosasdetios.views.page_not_found'
handler500 = 'cosasdetios.views.server_error'
