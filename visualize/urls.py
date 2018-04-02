from django.urls import path
from django.conf.urls import url

from . import views
from .views import jdata

urlpatterns = [
    path('', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    path('index3/', views.index3, name='index3'),
	path('visualize/', views.visualize, name='visualize'),
	url(r'^api/jdata', views.jdata, name='jdata'),
    url('heatmap', views.heatmap, name='heatmap'),
]
