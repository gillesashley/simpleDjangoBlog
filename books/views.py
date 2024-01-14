from django.views import generic
from .models import Book


# Create your views here.

class BookListView(generic.ListView):
    model = Book
