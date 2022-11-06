from django.urls import path

from .views import *  # Import all actions from views

urlpatterns = [
    path('', index, name='news'),
    path('<int:news_id>/', show_news, name='show_news'),
    path('questions', questions),
]
