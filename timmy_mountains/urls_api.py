from django.urls import path
from . import views

urlpatterns = [
    #  api  - mountain
    path('mountain/', views.create_mountain, name='mountain'),
    path('mountain/all', views.get_all_mountain, name='mountain'),
    #  api  - tunnel mountain
    path('mountain_tunnel/', views.create_mountain_tunnel, name='mountain_tunnel'),
    path('mountain_tunnel/all', views.get_all_mountain_tunnel, name='mountain_tunnel'),
    #  api  - not mountain
    path('not_mountain/', views.check_not_mountain, name='not_mountain'),

]
