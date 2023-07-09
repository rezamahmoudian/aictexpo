from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from .models import Company
from .serializers import CompanySerializer

# Create your views here.


class CompanyCreateListView(ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
