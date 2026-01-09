from django.contrib import admin
from .models import Author, Book, Reader, Loan


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'birth_year']
    search_fields = ['name', 'country']
    list_filter = ['country', 'birth_year']
    fieldsets = (
        ('Основна інформація', {
            'fields': ('name', 'country', 'birth_year')
        }),
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'isbn', 'pages', 'publication_year', 'is_available']
    search_fields = ['title', 'isbn', 'author__name']
    list_filter = ['publication_year', 'author', 'is_available']
    fieldsets = (
        ('Основна інформація', {
            'fields': ('title', 'author', 'isbn')
        }),
        ('Деталі', {
            'fields': ('pages', 'publication_year', 'is_available')
        }),
    )


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'books_count']
    search_fields = ['name', 'email']
    fieldsets = (
        ('Основна інформація', {
            'fields': ('name', 'email')
        }),
    )

    def books_count(self, obj):
        return obj.books.count()
    books_count.short_description = 'Кількість книг'


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ['reader', 'book', 'loan_date', 'return_date', 'status']
    search_fields = ['reader__name', 'book__title']
    list_filter = ['loan_date', 'return_date', 'reader', 'book__author']
    readonly_fields = ['loan_date']
    fieldsets = (
        ('Інформація про позику', {
            'fields': ('reader', 'book', 'loan_date', 'return_date')
        }),
    )

    def status(self, obj):
        if obj.return_date:
            return '✓ Повернута'
        return '⏳ На руках'
    status.short_description = 'Статус'
