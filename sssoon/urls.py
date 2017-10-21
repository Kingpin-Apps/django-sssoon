__author__ = 'Kingpin Apps'
from django.conf.urls import url
from . import views


urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
    # ex: /video
    url(r'^video/$', views.video, name='video'),
    # ex: /signup
    url(r'^signup/$', views.signup, name='signup'),
]
