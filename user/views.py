# from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from rest_framework.response import Response
# from rest_framework.parsers import JSONParser
from rest_framework import status
from . models import User
# from rest_framework.decorators import api_view
# from django.db.models import Q


# @api_view(['GET'])
def register(request):
    return render(request,"register.html")


# @api_view(['Post'])
# def register(request):
#     return render(request,"it works")
#     # return render(request, "register.html")

def adddata(request):
    content = {'status': 'accepted'}
    obj = User(name=request.POST.get('name'), email=request.POST.get('email'), password=request.POST.get('pswd'))
    obj.save()
    return Response(content)
