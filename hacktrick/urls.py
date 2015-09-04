from django.conf.urls import include, url

from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]