from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('healthreport',views.healthreport),
    url(r'^.*$', views.index)
]