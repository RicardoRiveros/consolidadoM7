from django.urls import path
from . import views

app_name = 'laboratorio'

urlpatterns = [
    path('', views.laboratorio_list, name='laboratorio_list'),
    path('create/', views.laboratorio_create, name='laboratorio_create'),
    path('update/<int:pk>/', views.laboratorio_update, name='laboratorio_update'),
    path('delete/<int:pk>/', views.laboratorio_delete, name='laboratorio_delete'),
    ]