from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from . models import User
from rest_framework.decorators import api_view
from django.db.models import Q
import requests
import re


# @api_view(['GET'])
def registeruser(request):
    return render(request,"register.html")


def login(request):
    return render(request, "login.html")


# @api_view(['Post'])
# def register(request):
#     return render(request,"it works")
#     # return render(request, "register.html")

# @api_view(['Post'])

@api_view(['POST'])
def register(request, *args, **kwargs):
    # print("inside register")
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    q = request.query_params.get('name', None)
    # print(q)
    if q == None:
        return JsonResponse({'message': 'give proper name'}, status=status.HTTP_400_BAD_REQUEST)
    q = request.query_params.get('email', None)
    # print(q)
    if q == None or not(re.match(regex,q)):
        return JsonResponse({'message': 'give proper email'}, status=status.HTTP_400_BAD_REQUEST)
    q = request.query_params.get('username', None)
    # print(q)
    if q == None:
        return JsonResponse({'message': 'give proper username'}, status=status.HTTP_400_BAD_REQUEST)
    q = request.query_params.get('password', None)
    if q == None:
        return JsonResponse({'message': 'give proper password'}, status=status.HTTP_400_BAD_REQUEST)
    a = User(name=request.query_params.get('name', None),
             email=request.query_params.get('email', None),
             phoneno=request.query_params.get('phoneno', None),
             password=request.query_params.get('password', None),
             username=request.query_params.get('username', None),
             gender=request.query_params.get('gender', None),
             dob=request.query_params.get('dob', None),
    )
    a.save()
    return JsonResponse({'message': 'Data Added'}, status=status.HTTP_200_OK)

def adddata(request):
    r = requests.post('http://127.0.0.1:8000/register/', params=request.POST)
    if r.status_code == 200:
        return render(request, "Dataadded.html")
    else:
        return render(request, "error.html")


@api_view(['POST'])
def login_API(request, *args, **kwargs):
    # print("ok i am in")
    print(request.query_params)
    email = request.query_params.get('email', None)
    if email == None:
        return JsonResponse({'message': 'Please Provide Username'}, status=status.HTTP_400_BAD_REQUEST)
    # print("ok i am in")
    password = request.query_params.get('password', None)
    if password == None:
        return JsonResponse({'message': 'Please Provide Password'}, status=status.HTTP_400_BAD_REQUEST)
    if User.objects.filter(email=email, password=password).exists():
        # print("user found")
        return JsonResponse({'message': 'Login Succes'}, status=status.HTTP_200_OK)
    else:
        # print("user not found")
        return JsonResponse({'message': 'Username Or Password Incoorect'}, status=status.HTTP_400_BAD_REQUEST)


def login_validate(request):
    r = requests.post('http://127.0.0.1:8000/login_API/', params=request.POST)
    if r.status_code == 200:
        return render(request, "homepage.html")
    else:
        return render(request, "login.html")

