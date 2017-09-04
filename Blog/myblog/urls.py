#coding=utf-8
from django.conf.urls import url
from myblog import views

urlpatterns = [
    url(r'^(home|lifestyle|piano|geek)', views.index, name='index'),
    url(r'^text/(\d+)$',views.text),
    url(r'^send_data$', views.send_data),
    url(r'^getArticals/(\d+)$', views.return_articals),
    url(r'^get_comments/(\d+)$', views.return_comments),
    url(r'^about/$',views.about),
    url(r'^artical/(\d+)$',views.show_artical,name='artical'),
    ]
