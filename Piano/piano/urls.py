from django.conf.urls import url
from piano import views

urlpatterns = [
    url(r'^home',views.index),
    url(r'^album/(.*)', views.list),
    url(r'^musicSheet/(.*)', views.show_sheet),
    url(r'^category/(.*)', views.category),

]