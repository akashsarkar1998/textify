from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('analyze/', views.analyze, name='analyze'),
    path('aboutme/', views.aboutme, name="aboutme"),
    path('contact/', views.contact, name="contact"),
]
