from django.urls import path

from . import views
from .views import HomeView, RegisterView, LoginView  # noqa

urlpatterns = [
    # Home
    path("", views.HomeView.as_view(), name="home"),
    # Register
    path("register/", views.RegisterView.as_view(), name="register"),
    # Login
    path("login/", views.LoginView.as_view(), name="login"),
]
