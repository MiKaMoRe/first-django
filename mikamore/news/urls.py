from django.urls import path

from .views import *  # Import all actions from views

urlpatterns = [
    path("", ListNews.as_view(), name="news"),
    path("<int:pk>/", DetailNews.as_view(), name="show_news"),
    path("new/", CreateNews.as_view(), name="new_news"),
    path("questions", questions),
]
