from django.urls import path, include

from . import views


urlpatterns = [
    path('ping', views.ping, name='ping'),
    path('cats', views.cat_list, name='cat_list'),
    path('cat', views.cat_create, name='cat_create'),
]
