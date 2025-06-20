from django.urls import path

from application import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('vision/', views.vision, name='vision'),
    path('mission/', views.mission, name='mission'),
    path('values/', views.core_values, name='core_values'),
    path('services/', views.services_list, name='services_list'),
    path('contact/', views.contact_view, name='contact'),
    path('team/', views.team, name='team'),
    path('spacnwal/', views.spacnwal, name= 'spacnwal'),
    path('abroad/', views.abroad, name='abroad'),
    ]