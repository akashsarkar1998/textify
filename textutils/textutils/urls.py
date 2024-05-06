"""
URL configuration for textutils project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# These videos are for videos till day 6:
# from django.contrib import admin
# from django.urls import path
# from . import views
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name='index'),
#     path('about/', views.about, name='about'),
#     path('text/', views.display_text, name='text'),
#     path('linkpages/', views.link_pages, name='linkpages'),
# ]

# # Videos from Day 7 to Day 9 // This pipeline is so good, So complete it later...
# from django.contrib import admin
# from django.urls import path
# from . import views
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('removepunc/', views.removepunc, name='removepunc'),
#     path('capitalizefirst/', views.capitalizefirst, name='capfirst'),
#     path('newlineremove/', views.newlineremove, name='newlineremove'),
#     path('spaceremover/', views.spaceremover, name='spaceremover'),
#     path('charcount', views.charcount, name='charcount'),
# ]

from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('analyze/', views.analyze, name='analyze'),
    path('aboutme/', views.aboutme, name="aboutme"),
    path('contact/', views.contact, name="contact"),
]