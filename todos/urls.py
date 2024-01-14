from django.urls import path
from .views import TodoList, DetailTodo

urlpatterns = [
    path('', TodoList.as_view(), name="todo-list"),
    path('<int:pk>/', DetailTodo.as_view(), name="todo-detail"),
]
