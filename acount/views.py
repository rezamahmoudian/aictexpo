from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

# Create your views here.


class UserListView(ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

