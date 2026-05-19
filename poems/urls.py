from django.urls import path

from . import views

app_name = 'poems'
urlpatterns = [
    path('', views.poem_list, name='poem_list'),
    path('<str:slug>/', views.poem_detail, name='poem_detail'),
]