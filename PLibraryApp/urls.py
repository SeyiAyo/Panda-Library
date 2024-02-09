from django.contrib import admin
from django.urls import path
from .views import helloView, addBookView, addBook, editBookView, editBook, deleteBookView
urlpatterns = [
    path('', helloView, name='helloView'),
    path('add-book/', addBookView),
    path('add-book/add/', addBook),
    path('edit-book/', editBookView),
    path('edit-book/edit/', editBook),
    path('delete-book/', deleteBookView),
]