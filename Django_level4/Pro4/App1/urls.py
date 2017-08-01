from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from App1 import views

# Template Tagging
app_name = 'App1'


urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^base/$',views.base,name='base'),
    url(r'^other/$',views.other,name='other'),
]
