from django.urls import path, include
from .views import create_user, list_all_users, get_user_by_id
from .views import add_new_book, list_all_books, get_book_by_id, assign_update_book_details
from .views import borrow_book, return_book, list_all_borrowed_books

user_urls = [
    path('create/', create_user, name='create_user'),
    path('list/', list_all_users, name = 'list_all_users'),
    path('<int:user_id>/', get_user_by_id, name = 'get_user_by_id'),
]

book_urls = [
    path('add/', add_new_book, name='add_new_book'),
    path('list/', list_all_books, name='list_all_books'),
    path('<int:book_id>/', get_book_by_id, name='get_book_by_id'),
    path('<int:book_id>/details/', assign_update_book_details, name="assign_update_book_details"),
]

borrowed_books_urls = [
    path('borrow/', borrow_book, name='borrow_book'),
    path('return/', return_book, name='return_book'),
    path('list/', list_all_borrowed_books, name='list_all_borrowed_books'),
]

urlpatterns = [
    path('users/', include((user_urls, 'users'), namespace='users')),
    path('books/', include((book_urls, 'books'), namespace='books')),
    path('borrowed-books/', include((borrowed_books_urls, 'borrowed_books'), namespace='borrowed_books')),
]