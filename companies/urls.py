from django.urls import path, include
from .views import CompanyCreateListView, ProductCreateListView, CompanyView
from rest_framework.urlpatterns import format_suffix_patterns

api_name = 'api'


urlpatterns = [
    path('companies/', CompanyCreateListView.as_view(), name='home'),
    path('companie/', CompanyView.as_view(), name='home1'),
    path('products/', ProductCreateListView.as_view(), name='product'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)