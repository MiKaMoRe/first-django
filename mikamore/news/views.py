from django.shortcuts import render
from django.http import HttpResponse

def questions(request):
    return HttpResponse('My questions')

def index(request):
    return HttpResponse('Hello world')
