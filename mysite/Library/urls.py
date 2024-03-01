from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.Hello_World, name="hello"),
    path("books", views.Insert_book, name="insert_book"),
    path("users", views.Insert_user, name="insert_user"),
    path("books/<int:id>", views.delete, name="delete_book_byid"),
    # path("books/borrower/<int:book_id>/<int:user_id>", views.borrow_book, name="borrow_book")
]
