from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /timmy_mountains/ for all kinds
    path('timmy_mountains/', views.index, name='index'),
    # ex: timmy_mountains/mountain/5
    path('timmy_mountains/mountain/<int:mountain_id>', views.mountain, name='mountain'),
    # ex: timmy_mountains/mountain_tunnel/5
    path('timmy_mountains/mountain_tunnel/<int:mountain_with_tunnels_id>', views.with_tunnels, name='mountain_tunnel')
]
