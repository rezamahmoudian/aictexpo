from django.urls import path, include
from .views import UserListView, UserDetailView

api_name = 'acount'

urlpatterns = [
    path('users/', UserListView.as_view(), name='home'),
    path('users/<int:pk>', UserDetailView.as_view(), name='user-detail'),
    # path('users/<int:pk>/hyper', UserDetailView.as_view(), name='home1'),
]
