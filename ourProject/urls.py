from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("Begin", views.begin, name="begin"),
    path("firstYear", views.firstYear, name="firstYear"),
    path("academcis", views.academics, name="academics"),
    path("profilePage", views.profilePage, name = "profilePage"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact")
]
