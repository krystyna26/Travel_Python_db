from django.conf.urls import url 
from . import views              
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),   
    url(r'^welcome$', views.welcome), 
    url(r'^buttonADD$', views.addTravel),
    url(r'^trip$', views.welcome), 
    url(r'^add$', views.add), 
    url(r'^join/(?P<trip_id>\d+)$', views.join),   
    # url(r'^trip$', views.trip),   
]