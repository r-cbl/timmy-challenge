from django.urls import path
from . import views


urlpatterns = [
    #  api  - mountain
    path('mountain/', views.create_mountain, name='mountain'),
    path('mountain/<int:mountain_id>', views.get_mountain, name='mountain'),
    path('mountain_tunnel/', views.create_mountain_tunnel, name='mountain_tunnel'),
    path('mountain_tunnel/<int:mountain_with_tunnels_id>', views.create_mountain_tunnel, name='mountain_tunnel'),
]