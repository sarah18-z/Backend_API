from django.shortcuts import render
from django.http import HttpResponse
from Library.models import Book


# Create your views here.
def Hello_World(request):
    return HttpResponse("Hello world !")


def Insert_book(request):
    book = Book(author="Souad", title="Django is cool")
    book.save()
    # book_details = {author: book.author etc etc}
    return ("le titre est :" + book.title + "/n l'auteur est :" + book.author)

