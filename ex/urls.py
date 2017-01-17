from django.conf.urls import url
from ex import views

urlpatterns = [
	url(r'^$', views.index),
]
