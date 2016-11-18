from django.conf.urls import url

from . import views

app_name = 'tracking'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^track/$', views.track_start, name='track_start'),
    url(r'^create/$', views.create_start, name='create_start'),
    url(r'^track_result/(?P<id>)$', views.track_id, name='track_id'),
    url(r'^create_result/$', views.create_pck, name='create_pck'),
]
