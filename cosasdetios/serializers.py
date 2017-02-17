from rest_framework import serializers

from podcast.models import Episode, Enclosure, Show


class ShowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Show
        fields = ('pk', 'title', 'subtitle', 'slug', 'image', 'description',
                  'author_name', 'explicit', 'complete', 'itunes')


class EpisodeSerializer(serializers.HyperlinkedModelSerializer):
    enclosure = serializers.PrimaryKeyRelatedField(read_only=True)
    show = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Episode
        fields = ('pk', 'show', 'title', 'slug', 'description', 'pub_date',
                  'subtitle', 'author_name', 'explicit', 'enclosure')


class EnclosureSerializer(serializers.HyperlinkedModelSerializer):
    episode = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Enclosure
        fields = ('pk', 'episode', 'file', 'type', 'poster')
