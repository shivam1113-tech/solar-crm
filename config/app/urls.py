from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
      path('login/', views.login),
      path('forgot/', views.forgot_password),
      path('verify-register/', views.verify_register),
]