from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("apps.users.urls")),   # routes for users
    path("books/", include("apps.books.urls")),   # new route for books
    path("", include("apps.main.urls")),          # home page
]

# serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
