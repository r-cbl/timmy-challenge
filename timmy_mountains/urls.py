from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /timmy_mountains/
    path('timmy_mountains/', views.index, name='index'),
    # ex: timmy_mountains/5/
    path('timmy_mountains/<int:mountain_id>', views.mountain, name='mountain'),
    # ex: /mountain_tunnel/5
    path('timmy_mountains/tunnel/<int:mountain_with_tunnels_id>', views.with_tunnels, name='mountain_tunnel'),
]