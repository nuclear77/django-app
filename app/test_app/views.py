from django.db.models import Avg, Min, Max
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

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


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/book/')
    else:
        form = BookForm()

    context = {'form': form}
    return render(request, 'add_book.html', context)


def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/home/', book_id=book_id)
    else:
        form = BookForm(instance=book)

    return render(request, 'edit_book.html', {'form': form, 'book': book})