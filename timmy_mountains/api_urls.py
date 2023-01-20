from django.urls import path
from . import views


urlpatterns = [
    #  api  - mountain
    path('mountain/', views.create_mountain, name='mountain'),
    path('mountain/<int:mountain_with_tunnels_id>', views.create_mountain, name='mountain'),
    #  todo: api  - mountain with tunnel
]