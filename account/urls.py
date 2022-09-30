from django.urls import path
from .import views

urlpatterns = [
    path('',views.RegisterPage,name='register'),
    path('login/',views.LoginPage,name='login'),
    path('profile/',views.ProfilePage,name='profile'),
    path('logout/',views.LogoutUser,name='logout'),
]