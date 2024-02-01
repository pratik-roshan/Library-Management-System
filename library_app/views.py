from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User, Book, BookDetails, BorrowedBooks
from .serializers import UserSerializer, BookSerializer, BookDetailsSerializer, BorrowedBooksSerializer

# USER API 
# Create a New User 
@api_view(['POST'])
def create_user(request):
    """
    API endpoint to create a new user.

    Args:
        request (HttpRequest): The request object.

    Returns:
        Response: JSON response with user data or error.
    """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_all_users(request):
    """
    API endpoint to retrieve a list of all users.

    Args:
        request (HttpRequest): The request object.

    Returns:
        Response: JSON response with a list of users.
    """
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_user_by_id(request, user_id):
    """
    API endpoint to fetch user details by user ID.

    Args:
        request (HttpRequest): The request object.
        user_id (int): User ID.

    Returns:
        Response: JSON response with user details or error.
    """
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
    """
    API endpoint to add a new book.

    Args:
        request (HttpRequest): The request object.

    Returns:
        Response: JSON response with book data or error.
    """
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# List all Books 
@api_view(['GET'])
def list_all_books(request):
    """
    API endpoint to retrieve a list of all books.

    Args:
        request (HttpRequest): The request object.

    Returns:
        Response: JSON response with a list of books.
    """
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

# Get Book by ID 
@api_view(['GET'])
def get_book_by_id(request, book_id):
    """
    API endpoint to fetch book details by book ID.

    Args:
        request (HttpRequest): The request object.
        book_id (int): Book ID.

    Returns:
        Response: JSON response with book details or error.
    """
    try:
        book = Book.objects.get(BookID=book_id)
    except Book.DoesNotExist:
        return Response({"error": "Book not found"}, status=404)

    serializer = BookSerializer(book)
    return Response(serializer.data)

# Assign/Update Book Details 
@api_view(['POST'])
def assign_update_book_details(request, book_id):
    """
    API endpoint to assign or update book details.

    Args:
        request (HttpRequest): The request object.
        book_id (int): Book ID.

    Returns:
        Response: JSON response with book details or error.
    """
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
    """
    API endpoint to record the borrowing of a book.

    Args:
        request (HttpRequest): The request object.

    Returns:
        Response: JSON response with borrowed book data or error.
    """
    serializer = BorrowedBooksSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Return a Book 
@api_view(['PUT'])
def return_book(request, borrow_id):
    """
    API endpoint to update the system when a book is returned.

    Args:
        request (HttpRequest): The request object.
        borrow_id (int): Borrowed book ID.

    Returns:
        Response: JSON response with updated borrowed book data or error.
    """
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
    """
    API endpoint to list all books currently borrowed from the library.

    Args:
        request (HttpRequest): The request object.

    Returns:
        Response: JSON response with a list of borrowed books.
    """
    borrowed_books = BorrowedBooks.objects.all()
    serializer = BorrowedBooksSerializer(borrowed_books, many=True)
    return Response(serializer.data)
