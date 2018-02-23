from django.conf.urls import url
from appTwo import views

app_name = 'appTwo'

urlpatterns = [
	url(r'^$', views.users, name = 'users'),
	url(r'^list', views.index, name = 'users_list'),
]