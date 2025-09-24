from django.shortcuts import render, get_object_or_404
from .models import Book

def book_list(request):
    """Display a list of all published books."""
    books = Book.objects.filter(is_published=True).order_by("-created_at")
    return render(request, "books/book_list.html", {"books": books})

def book_detail(request, pk):
    """Display details of a specific book."""
    book = get_object_or_404(Book, pk=pk, is_published=True)
    return render(request, "books/book_detail.html", {"book": book})
