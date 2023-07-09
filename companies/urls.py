from django.urls import path, include
from .views import CompanyCreateListView

api_name = 'api'


urlpatterns = [
    path('companies/', CompanyCreateListView.as_view(), name='home')
]

