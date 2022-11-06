from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import News, Category
from .forms import NewsForm


def questions(request):
    return HttpResponse("My questions")


def new_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, "news/new.html", {"form": form})


def show_news(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, "news/show_news.html", {"news": news})


def index(request):
    news = News.objects.all()
    return render(request, "news/index.html", {"news": news})


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    return render(request, "news/category.html", {"news": news})
