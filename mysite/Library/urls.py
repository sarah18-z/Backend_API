from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.Hello_World, name="hello"),
    path("books", views.Insert_book, name="insert_book"),
    path("books/<int:id>", views.delete)
]
