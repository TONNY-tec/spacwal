from django.urls import path

from application import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('vision/', views.vision, name='vision'),
    path('mission/', views.mission, name='mission'),
    path('values/', views.core_values, name='core_values'),
    path('services/', views.services_list, name='services_list'),
    ]