from http.client import HTTPException
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from Library.models import Book,User
from Library.serializers import BookSerializer, UserSerializer

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
def Insert_user(request):
    # add user
    if request.method == "POST":
        data = JSONParser().parse(request)

        User_serializer = UserSerializer(data=data)
        if User_serializer.is_valid():
            User_serializer.save()
        else:
            return HTTPException()
        
        return JsonResponse(User_serializer.data)
    
    # get all users
    if request.method == "GET":
        users = User.objects.all()
        User_serializer = UserSerializer(users, many=True)
        return JsonResponse(User_serializer.data, safe=False)

@csrf_exempt
def delete(request, id):
    # get book by id
    if request.method == "GET":
        book = Book.objects.get(id=id)
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data)
    # delete book by id 
    elif request.method == "DELETE":
        book = Book.objects.get(id=id)
        book.delete()
        return JsonResponse({'success': True})

       
# @csrf_exempt        
# def borrow_book(request, title, user_name):
#     book = Book.objects.get(title= title)
#     user = User.objects.get(user_name=user_name)

#     if request.method == 'POST':
#         book.is_borrowed = True
#         book.borrower = user
#         book.save()

#         book_serializer = BookSerializer(book)
#         user_serializer = UserSerializer(user)

#         return JsonResponse({
#             'message': f'Book "{book.title}" is now borrowed by {user.first_name} {user.last_name}',
#             'book': book_serializer.data,
#             'borrower': user_serializer.data,
#         })
#     return HTTPException({'error': 'Invalid request method'}, status=400)  

            
        
