from django.shortcuts import render
from rest_framework import viewsets

from podcast.models import Episode, Enclosure, Show
from .serializers import EpisodeSerializer, ShowSerializer, EnclosureSerializer


class ShowViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Show.objects.all().order_by('-pk')
    serializer_class = ShowSerializer


class EpisodeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Episode.objects.all().order_by('-pub_date')
    serializer_class = EpisodeSerializer


class EnclosureViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Enclosure.objects.all().order_by('-pk')
    serializer_class = EnclosureSerializer


# HTTP Error 400
def bad_request(request):
    response = render(request, '400.html')
    response.status_code = 400
    return response


# HTTP Error 403
def permission_denied(request):
    response = render(request, '403.html')
    response.status_code = 403
    return response


# HTTP Error 404
def page_not_found(request):
    response = render(request, '404.html')
    response.status_code = 404
    return response


# HTTP Error 500
def server_error(request):
    response = render(request, '500.html')
    response.status_code = 500
    return response
