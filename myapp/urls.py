from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^api/like$', views.like_api),
    url(r'^action/post$', views.post),
    url(r'^action/like$', views.like),
    url(r'^api/load$', views.load),
]