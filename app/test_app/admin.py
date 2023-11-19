from django.contrib import admin
from .models import Author, Library, LibraryBook, Book


class CustomAuthorAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name')
    list_display = ('first_name', 'last_name')


class CustomLibraryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'address')


class CustomLibraryBookAdmin(admin.ModelAdmin):
    search_fields = ('library__name',)


class CustomBookAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'year', 'author', 'library')


admin.site.register(Library, CustomLibraryAdmin)
admin.site.register(LibraryBook, CustomLibraryBookAdmin)
admin.site.register(Book, CustomBookAdmin)
admin.site.register(Author, CustomAuthorAdmin)