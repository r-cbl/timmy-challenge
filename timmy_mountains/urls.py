from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_mountain, name='index'),
    path('timmy_mountains/', views.index_mountain, name='index'),
]
