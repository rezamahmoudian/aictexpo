from django.urls import path, include
from .views import CompanyCreateListView, ProductCreateListView

api_name = 'api'


urlpatterns = [
    path('companies/', CompanyCreateListView.as_view(), name='home'),
    path('products/', ProductCreateListView.as_view(), name='home'),
]

