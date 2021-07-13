from django.urls import path
from . import views


urlpatterns = [
    path('registeruser/', views.registeruser),
    path('registeruser/adddata/', views.adddata),
    path('register/', views.register),
    path('', views.login),
    path('login_API/', views.login_API),
    path('login_validate/', views.login_validate)
    # path('seacrh/', views.seacrh),
    # path('', views.registartion_form),
]
