from django.urls import path
from . import views

urlpatterns = [
    path('', views.todos, name='todos'),
    path('add-todo/', views.add_todo, name='add_todo'),
    path('update/<int:pk>/', views.update_todo, name='update_todo'),
    path('delete/<int:pk>/', views.delete_todo, name='delete_todo'),
    path('edit/<int:pk>/', views.edit_todo, name='edit_todo'),

]
