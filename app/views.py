from django.urls import reverse_lazy

from app.models import New

# CRUD
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView
)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages



class NewsListView(LoginRequiredMixin, ListView):
    template_name = "app/read_news.html"
    model = New
    context_object_name = "news"
    paginate_by = 5


    def get_queryset(self, *args, **kwargs):
        search = self.request.GET.get("search")

        qs = super(NewsListView, self).get_queryset(*args, **kwargs)
        qs = qs.filter(creator=self.request.user).order_by("-created_at")

        if search:
            qs = qs.filter(title__search=search)

        return qs


class NewsCreateView(LoginRequiredMixin, CreateView):
    template_name = "app/news_create.html"
    model = New
    fields = ("title", "author", "facebook_link", "twitter_link", "linkedin_link", "content", "status")
    success_url = reverse_lazy("read_news")


    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form=form)


class NewsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "app/news_update.html"
    model = New
    fields = ("title", "author", "facebook_link", "twitter_link", "linkedin_link", "content", "status")
    success_url = reverse_lazy("read_news")
    context_object_name = "new"

    def test_func(self):
        return self.request.user == self.get_object().creator



class NewsDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "app/news_delete.html"
    model = New
    success_url = reverse_lazy("read_news")
    context_object_name = "new"

    def test_func(self):
        return self.request.user == self.get_object().creator

    def post(self, request, *args, **kwargs):
        messages.warning(request, f'Успешно изтрихте новината "{self.get_object()}".', extra_tags="danger")

        return super().post(request, *args, **kwargs)
