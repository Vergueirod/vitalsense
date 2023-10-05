from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerUsers, name="register" ),
    path('login/', views.authLogin, name="login" ),

]