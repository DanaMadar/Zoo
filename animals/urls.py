from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_animal_vies, name='all_animals'),
    path('<int:id>/', views.all_animal_vies, name='all_animals')
]
