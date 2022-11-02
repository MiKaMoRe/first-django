from django.shortcuts import render
from django.http import HttpResponse
from .models import News

def questions(request):
    return HttpResponse('My questions')

def index(request):
    news = News.objects
    context = { 'news': news }
    return render(request, 'news/index.html', context)
