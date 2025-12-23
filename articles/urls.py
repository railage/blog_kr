from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('create/', views.article_create, name='article_create'),
    path('<int:id>/edit/', views.article_edit, name='article_edit'),
    path('<int:id>/delete/', views.article_delete, name='article_delete'),
]