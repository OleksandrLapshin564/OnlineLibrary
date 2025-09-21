from django.contrib.auth import get_user_model
from apps.books.models import Author, Genre, Book
from apps.comments.models import Comment

CustomUser = get_user_model()

user, _ = CustomUser.objects.get_or_create(
    username="testuser",
    defaults={"email": "testuser@example.com"}
)

author, _ = Author.objects.get_or_create(name="Test Author")
genre, _ = Genre.objects.get_or_create(name="Test Genre", slug="test-genre")

book, _ = Book.objects.get_or_create(
    title="Test Book",
    slug="test-book",
    defaults={"description": "This is a test book."}
)
book.authors.add(author)
book.genres.add(genre)

Comment.objects.get_or_create(
    user=user,
    book=book,
    content="This is a test comment."
)

# --- Counters ---
print("Users:", CustomUser.objects.count())
print("Books:", Book.objects.count())
print("Comments:", Comment.objects.count())
