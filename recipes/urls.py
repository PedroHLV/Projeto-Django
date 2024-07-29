from django.http import HttpResponse
from django.urls import path
from django.contrib import admin
from recipes.views import home
from recipes import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<int:id>/', views.recipe, name='recipe'),
]