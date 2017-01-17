from django.conf.urls import url
from ex import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^sign_in$', views.sign_in),
	# url(r'^log_in$', views.log_in),
]
