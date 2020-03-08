from django.urls import path
from . import views

urlpatterns = [
    path('', views.character_list, name='character_list'),
    path('character/<int:pk>/', views.character_detail, name='character_detail'),
]
