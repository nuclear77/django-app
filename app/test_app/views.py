from django.db.models import Avg, Min, Max
from django.shortcuts import render
from .models import Book

def home(request):
    average_price = Book.objects.aggregate(avg_price=Avg('price'))
    min_price = Book.objects.aggregate(min_price=Min('price'))
    max_price = Book.objects.aggregate(max_price=Max('price'))
    total_books = Book.objects.count()

    context = {
        'average_price': average_price['avg_price'],
        'min_price': min_price['min_price'],
        'max_price': max_price['max_price'],
        'total_books': total_books,
    }

    return render(request, 'home.html', context)