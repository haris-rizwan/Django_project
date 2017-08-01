from django.conf.urls import url,include
from App1 import views


app_name = 'App1'

urlpatterns=[
    url(r'^registration/$',views.registration,name='registration'),
    url(r'^user_login/$',views.user_login,name='user_login')

]
