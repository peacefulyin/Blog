#coding=utf-8
from django.conf.urls import url
from myblog import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^text/$',views.text),
    url(r'^test/$', views.test),
    url(r'^send_data$', views.send_data),
    url(r'^getArticals/(\d+)$', views.return_articals),
    url(r'^get_comments/(\d+)$', views.return_comments),
    url(r'^about/$',views.about),
    url(r'^artical/(.*)$',views.show_artical),
    ]
