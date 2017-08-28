#coding=utf-8
from django.conf.urls import url
from myblog import views

urlpatterns = [
    url(r'^index/(\d+)', views.index),
    url(r'^text/$',views.text),
    url(r'^about/$',views.about),
    url(r'^artical/(.*)$',views.show_artical),
    ]
