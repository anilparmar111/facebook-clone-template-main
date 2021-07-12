from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register),
    path('register/adddata/', views.adddata),
    # path('seacrh/', views.seacrh),
    # path('', views.registartion_form),
]
