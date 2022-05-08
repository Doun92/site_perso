from django.urls import path

from . import views

# Cela permet aux templates de repérer les bons URLs (particulièrement utile lorsqu'il y aura de nombreuses app)
app_name = 'webpages'

# URL management for the todo list
urlpatterns = [
    path('', views.homepage_fr, name='homepage_fr'),
    path('fr', views.homepage_fr, name='homepage_fr'),
    path('en', views.homepage_en, name='homepage_en'),
    path('cv', views.cv, name='cv'),
]