from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("", views.book_list, name="book_list"),          # List all books
    path("<int:pk>/", views.book_detail, name="book_detail"),  # Book detail page
]
