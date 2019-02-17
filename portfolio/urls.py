from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name="portfolio"),
    path('newphoto/', views.newphoto, name="newphoto"),
    ]