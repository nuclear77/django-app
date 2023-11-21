
from django.db import transaction
from faker import Faker
from test_app.models import AbstractAuthor, Library, Author, Book, LibraryBook

fake = Faker()


@transaction.atomic
def generate_fake_data(num_authors, num_libraries, num_books):
    # Создание фейковых авторов
    for _ in range(num_authors):
        first_name = fake.first_name()
        last_name = fake.last_name()
        Author.objects.create(first_name=first_name, last_name=last_name)

    # Создание фейковых библиотек
    for _ in range(num_libraries):
        name = fake.company()
        address = fake.address()
        Library.objects.create(name=name, address=address)

    # Получение всех авторов и библиотек
    authors = Author.objects.all()
    libraries = Library.objects.all()

    # Создание фейковых книг
    for _ in range(num_books):
        title = fake.catch_phrase()
        year = fake.random_int(min=1900, max=2023)
        author = fake.random_element(authors)
        library = fake.random_element(libraries)
        price = fake.pydecimal(min_value=0, max_value=100000, right_digits=2)
        Book.objects.create(title=title, year=year, author=author, library=library, price=price)

    # Создание связей между библиотеками и книгами
    for library in libraries:
        books = Book.objects.filter(library=library)
        library_book = LibraryBook.objects.create(library=library)
        library_book.books.set(books)


# Генерация фейковых данных
generate_fake_data(num_authors=10, num_libraries=5, num_books=50)