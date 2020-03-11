from django.urls import path
from . import views

urlpatterns = [
    path('', views.character_list_view, name='character_list'),
    path('filter/', views.character_filter_view, name='character_filter'),
    path('character/<int:pk>/', views.character_detail, name='character_detail'),
]
