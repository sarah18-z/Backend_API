from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.Hello_World, name="hello"),
    path('insert_book', views.Insert_book, name="isert_book"),
]
