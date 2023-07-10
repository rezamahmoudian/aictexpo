from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from .models import Company, Product
from .serializers import CompanySerializer, ProductSerializer
from .permissions import BasePermission, IsAuthorOrReadOnly, IsStaffOrReadOnly

# Create your views here.


class CompanyCreateListView(ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsStaffOrReadOnly]


class ProductCreateListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsStaffOrReadOnly]

