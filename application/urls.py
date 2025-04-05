from django.urls import path

from application import views

urlpatterns = [
    path('index/', views.index, name='index'),
    ]