from django.db import models
from django.conf import settings
from apps.books.models import Book

class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    content = models.TextField()
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replies'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment by {self.user} on {self.book}"


class ReadingProgress(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )
    position = models.IntegerField(default=0)  # character offset or page number
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'book')
        verbose_name = 'Reading Progress'
        verbose_name_plural = 'Reading Progresses'

    def __str__(self):
        return f"{self.user} progress in {self.book}: {self.position}"
