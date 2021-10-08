from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addTodo', views.addTodo),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
]
