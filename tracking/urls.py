from django.conf.urls import url

from . import views

app_name = 'tracking'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^track/$', views.track, name='track'),
    url(r'^new/$', views.new, name='new'),
]
