#coding=utf-8
from django.conf.urls import url
from myblog import views

urlpatterns = [
    url(r'^index/(\d+)', views.index),
    url(r'^text/$',views.text),
    url(r'^test/$', views.test),
    url(r'^json/$', views.getjson),
    url(r'^about/$',views.about),
    url(r'^artical/(.*)$',views.show_artical),
    ]
