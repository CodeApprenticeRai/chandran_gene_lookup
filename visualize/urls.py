from django.urls import path
from django.conf.urls import url

from . import views
from .views import jdata

urlpatterns = [
    path('', views.index, name='index'),
	path('visualize/', views.visualize, name='visualize'),
	url(r'^api/jdata', views.jdata, name='jdata')
]
