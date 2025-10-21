from django.urls import path, include
from . import views

app_name = 'user_auth'
urlpatterns = [
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name = 'logout')
    ]