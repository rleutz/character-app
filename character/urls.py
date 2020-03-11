from django.urls import path
from . import views

urlpatterns = [
    path('', views.character_list, name='character_list'),
    path('filter/', views.character_filter, name='character_filter'),
    path('character/<int:pk>/', views.character_detail, name='character_detail'),
]
