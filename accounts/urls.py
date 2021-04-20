from django.urls import path

from .views import (home_view, login_view, register_view, terms_view, logout_view, profile_view)

urlpatterns = [
    path('', home_view, name="home"),
    path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
    path('profile/<str:username>/', profile_view, name="profile"),
    path('terms/', terms_view, name="terms"),
    path('logout/', logout_view, name="logout"),
]
