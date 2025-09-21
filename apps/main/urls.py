from django.urls import path
from .views import home, CustomLoginView, CustomLogoutView

app_name = "main"

urlpatterns = [
    path("", home, name="home"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
]
