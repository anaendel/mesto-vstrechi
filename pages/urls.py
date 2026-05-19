from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.poems, name='poems'),
    path('materials/', views.materials, name='materials'),
]