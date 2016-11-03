from django.conf import settings
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import handler400, handler403, handler404, handler500

urlpatterns = [
        url(r'^adminpod/', admin.site.urls),
        url(r'^', include('podcast.urls')),
        url(r'^historias/', include('posts.urls')),
        ]

# urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler400 = 'papeonerd.views.bad_request'
handler403 = 'papeonerd.views.permission_denied'
handler404 = 'papeonerd.views.page_not_found'
handler500 = 'papeonerd.views.server_error'
