from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('getStart',views.getStart),
    path('login',views.login),
    path('getYzm', views.getYzm),
    path('getSettings',views.getSettings),
    path('getKb',views.getKb),
    path('getIcs',views.getIcs),
    path('getIcsDashboard',views.getIcsDashboard),
    url(r'^.*$', views.index)
]