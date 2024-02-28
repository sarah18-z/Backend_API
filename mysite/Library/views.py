from http.client import HTTPException
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from Library.models import Book
from Library.serializers import BookSerializer

# to avoid TypeErrors : must receive a Request and return a Response
def Hello_World(request):
    return HttpResponse("Hello World")

@csrf_exempt
def Insert_book(request):
    # add book
    if request.method == "POST":
        data = JSONParser().parse(request)

        book_serializer = BookSerializer(data=data)
        if book_serializer.is_valid():
            book_serializer.save()
        else:
            return HTTPException()
        
        return JsonResponse(book_serializer.data)
    
    # get all books
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)
    
@csrf_exempt
def delete(request, id):
    if request.method == "DELETE":
        book = Book(id=id)
        book.delete()
        
        
        
