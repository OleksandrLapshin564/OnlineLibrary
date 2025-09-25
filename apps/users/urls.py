from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from .views.login import login_view
from .views.register import register_view

app_name = "users"

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", LogoutView.as_view(next_page="main:home"), name="logout"),
    path("register/", register_view, name="register"),
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(
            template_name="users/password_change.html",
            success_url=reverse_lazy("users:login"),
        ),
        name="password_change",
    ),
]
