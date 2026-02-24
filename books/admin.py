from django.contrib import admin

# Register your models here.
from .models import Book, BookAuthor, BookReview, Author

class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'isbn')
    list_display = ('isbn', 'title', 'description')

class AuthorAmin(admin.ModelAdmin):
    pass


class BookAuthorAmin(admin.ModelAdmin):
    pass

class BookReviewAmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAmin)
admin.site.register(BookAuthor, BookAuthorAmin)
admin.site.register(BookReview, BookReviewAmin)