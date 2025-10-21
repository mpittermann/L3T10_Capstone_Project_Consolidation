from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "members"
urlpatterns = [
    path('members', views.member_list, name="member_list"),
    path('register', views.register, name="register")
    ]