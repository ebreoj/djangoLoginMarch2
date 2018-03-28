from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^main', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^dashboard$', views.success),
    url(r'^posts/additem$', views.additem),
    url(r'^create$', views.createitem),
    url(r'^index2$', views.new),
    url(r'^logout$', views.logout),
    url(r'^(?P<id>\d+)$', views.showitem),
    url(r'^remove/(?P<id>\d+)$', views.removeitem),
    url(r'^add/(?P<id>\d+)$', views.addtowishlist),
    url(r'^delete/(?P<id>\d+)$', views.delete), 
]

