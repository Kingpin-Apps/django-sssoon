__author__ = 'Kingpin Apps'

from django.urls import path

from . import views
from .apps import SssoonConfig

app_name = SssoonConfig.name

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    # ex: /video
    path('video/', views.video, name='video'),
    # ex: /signup
    path('signup/', views.signup, name='signup'),
]
