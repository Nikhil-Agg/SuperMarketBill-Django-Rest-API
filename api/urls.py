from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('items/', views.getItems, name='get-items'),
    path('add/', views.addItems, name='add-items')
]