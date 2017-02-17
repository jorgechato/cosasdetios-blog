from __future__ import unicode_literals
import os

from django.db import models
from django.core.urlresolvers import reverse
from slugify import slugify
from ckeditor.fields import RichTextField
from django.utils import timezone
from emoji import Emoji


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    slug = slugify(instance.title)
    today = timezone.now().strftime('%Y-%b-%d')
    filename = "{}/{}/cover.{}".format(today, slug, ext)
    return os.path.join('historias/', filename)


class Category(models.Model):
    order = models.IntegerField()
    title = models.CharField(max_length=140)
    slug = models.SlugField(max_length=140, blank=True, editable=False)
    keywords = models.TextField(blank=True, null=True)
    description = models.CharField(max_length=240, blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.slug

    def __unicode__(self):
        return unicode(self.slug)

    def save(self, *arg, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*arg, **kwargs)

    def get_absolute_url(self):
        return reverse('articles:category', kwargs={'slug': self.slug})

    class Meta:
        unique_together = ('title',)


class SideBar(models.Model):
    title = models.CharField(max_length=140, blank=True, null=True)
    order = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    categories_id = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title

    def save(self, *arg, **kwargs):
        self.content = Emoji.replace(self.content)
        self.title = Emoji.replace(self.title)
        super(SideBar, self).save(*arg, **kwargs)

    class Meta:
        unique_together = ('title', 'order')


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    categories_id = models.ForeignKey(Category, related_name='Posts')
    title = models.CharField(max_length=240)
    slug = models.SlugField(max_length=240, blank=True, editable=False)
    content = RichTextField()
    published_at = models.DateTimeField()
    public = models.BooleanField(default=True)
    thumbnail = models.ImageField(upload_to=content_file_name, blank=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return unicode(self.slug)

    def save(self, *arg, **kwargs):
        self.slug = slugify(self.title)
        self.content = Emoji.replace(self.content)
        self.title = Emoji.replace(self.title)
        super(Post, self).save(*arg, **kwargs)

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'slug': self.slug, 'categories_id': self.categories_id})

    class Meta:
        unique_together = ('title',)
        ordering = ('-published_at',)
