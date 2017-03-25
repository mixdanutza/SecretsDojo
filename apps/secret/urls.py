from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.index, name="index"),
	url(r"^process$", views.process, name="process"),
	url(r"^delete/(?P<id>\d+)$", views.delete, name="delete"),
	url(r"^like/(?P<id>\d+)$", views.like, name="like"),
	url(r"^popular$", views.popular, name="popular")
]