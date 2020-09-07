from django.urls import path, include
from . import views

urlpatterns = [
    path('destinations', views.get_destination, name='destinations'),
    path('<int:destination_id>', views.detail, name='detail'),
]
