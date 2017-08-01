from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from App3 import views


urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^forms',views.Info_Form,name='form')
]
