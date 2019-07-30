from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializer
# Create your views here.

class BusinessViewset(viewsets.ModelViewSet):
    queryset = models.Business.objects.all()
    serializer_class = serializer.BusinessSerializer

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializer.EmployeeSerializer

class EmployedViewset(viewsets.ModelViewSet):
    queryset = models.Employed.objects.all()
    serializer_class = serializer.EmployedSerializer
