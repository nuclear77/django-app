from django.urls import path
from . import views
from .views import edit_book

urlpatterns = [
    path('home/', views.home),
    path('book/', views.add_book),
    path('books/<int:book_id>/edit/', edit_book, name='edit_book'),
]