from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# Home page
def home(request):
    return render(request, "main/home.html")

# Login view
class CustomLoginView(LoginView):
    template_name = "main/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("main:home")

# Logout view
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("main:home")
