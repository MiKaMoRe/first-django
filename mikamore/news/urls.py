from django.urls import path

from .views import * # Import all actions from views

urlpatterns = [
    path('', index),
    path('questions', questions),
]