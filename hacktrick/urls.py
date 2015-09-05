from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name="user_login"),
    url(r'^logout/$', views.user_logout, name="user_logout"),
    url(r'^scans/$', views.scans, name="scans"),
    url(r'^get-scans/$', views.get_scans, name="get_scans"),
    url(r'^scan-result/(?P<id>[0-9]{1,4})$', views.scan_result, name="scan_result"),
]