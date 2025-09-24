from django.contrib import admin
from .models import Author, Genre, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")   # what to show in the list
    search_fields = ("name",)       # search by name
    ordering = ("name",)            # sorting


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    prepopulated_fields = {"slug": ("name",)}  # auto-generation of slug from name
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_published", "created_at")  # columns in the list
    list_filter = ("is_published", "created_at", "genres")        # filters on the right
    search_fields = ("title", "description")                      # search
    ordering = ("-created_at",)                                   # sorting
    prepopulated_fields = {"slug": ("title",)}                    # slug autogeneration
    filter_horizontal = ("authors", "genres")                     # convenient choice ManyToMany
    date_hierarchy = "created_at"                                 # date navigation
