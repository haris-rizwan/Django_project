from django.conf.urls import url
from AppTwo import views

urlpatterns = [
 url(r'^$',views.index,name='index'),
 url(r'^user',views.user,name='user'),
 url(r'^signup',views.signUp,name='signup')

]
