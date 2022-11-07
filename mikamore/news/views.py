from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import News, Category
from .forms import NewsForm


class ListNews(ListView):
    model = News
    template_name = "news/index.html"
    context_object_name = "news"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Новости"
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class ListNewsByCategory(ListView):
    model = News
    template_name = "news/index.html"
    context_object_name = "news"
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = get_object_or_404(Category, pk=self.kwargs["category_id"])
        return context

    def get_queryset(self):
        return News.objects.filter(
            category_id=self.kwargs["category_id"], is_published=True
        )


class DetailNews(DetailView):
    model = News
    template_name = "news/show_news.html"
    context_object_name = "news"


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = "news/new.html"
    # success_url = reverse_lazy('root')


def questions(request):
    return HttpResponse("My questions")
