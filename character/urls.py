from django.urls import path
from . import views

urlpatterns = [
    path('', views.character_list_view.as_view(), name='character_list'),
    path('urls/', views.url_list_view.as_view(), name='url_list'),
    path('filter/', views.character_filter_view.as_view(), name='character_filter'),
    path('character/<int:pk>/', views.character_detail, name='character_detail'),
    path('character/<int:pk>/edit/', views.character_edit, name="character_edit"),
]
