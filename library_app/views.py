from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer
from .models import Book
from .serializers import BookSerializer
from .models import Book, BookDetails
from .serializers import BookDetailsSerializer
from .models import BorrowedBooks
from .serializers import BorrowedBooksSerializer

# Create your views here.

# USER API 
# Create a New User 
@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_user_by_id(request, user_id):
    try:
        user = User.objects.get(UserID=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

    serializer = UserSerializer(user)
    return Response(serializer.data)


# BOOK APIs 

# Add a New Book 
@api_view(['POST'])
def add_new_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# List all Books 
@api_view(['GET'])
def list_all_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

# Get Book by ID 
@api_view(['GET'])
def get_book_by_id(request, book_id):
    try:
        book = Book.objects.get(BookID=book_id)
    except Book.DoesNotExist:
        return Response({"error": "Book not found"}, status=404)

    serializer = BookSerializer(book)
    return Response(serializer.data)

# Assign/Update Book Details 
@api_view(['POST'])
def assign_update_book_details(request, book_id):
    try:
        book = Book.objects.get(BookID=book_id)
    except Book.DoesNotExist:
        return Response({"error": "Book not found"}, status=404)

    serializer = BookDetailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(BookID=book)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Borrowed Books API 
@api_view(['POST'])
def borrow_book(request):
    serializer = BorrowedBooksSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Return a Book 
@api_view(['PUT'])
def return_book(request, borrow_id):
    try:
        borrowed_book = BorrowedBooks.objects.get(id=borrow_id)
    except BorrowedBooks.DoesNotExist:
        return Response({"error": "Borrowed book not found"}, status=404)

    serializer = BorrowedBooksSerializer(borrowed_book, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# List all Borrowed Books 
@api_view(['GET'])
def list_all_borrowed_books(request):
    borrowed_books = BorrowedBooks.objects.all()
    serializer = BorrowedBooksSerializer(borrowed_books, many=True)
    return Response(serializer.data)