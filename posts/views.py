from django.utils import timezone
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from cosasdetios.settings import api

from .models import Post


class ThoughtsListView(TemplateView):
    template_name = "thoughts_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ThoughtsListView, self).get_context_data(*args, **kwargs)
        page = 0
        if self.request.GET.get('page', None):
            page = int(self.request.GET.get('page'))
            page = 0 if page == 0 else page - 1

        # 825652419891695617  @beerwhisper
        # 202708941           @orggue
        context['tweets'] = api.GetUserTimeline(user_id=202708941,
                                                include_rts=False,
                                                count=20,
                                                max_id=page)
        return context


class PostDetailView(DetailView):
    model = Post


class PostListView(ListView):
    model = Post
    paginate_by = 5

    def get_queryset(self):
        queryset = super(PostListView, self).get_queryset()
        queryset = queryset.filter(categories_id__slug=self.kwargs['slug'],
                                   public=True,
                                   published_at__lte=timezone.now())
        return queryset
