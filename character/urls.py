from django.urls import path
from . import views

urlpatterns = [
    path('', views.character_list_view.as_view(), name='character_list'),
    path('url/', views.url_list_view.as_view(), name='url_list'),
    path('url/new/', views.url_new, name='url_new'),
    path('filter/', views.character_filter_view.as_view(), name='character_filter'),
    path('character/urls/<int:pk>/', views.url_detail, name='url_detail'),
    path('character/urls/<int:pk>/edit/', views.url_edit, name="url_edit"),
    path('character/urls/<int:pk>/remove/', views.url_remove, name="url_remove"),
    path('character/<int:pk>/', views.character_detail, name='character_detail'),
    path('character/<int:pk>/edit/', views.character_edit, name="character_edit"),
]
