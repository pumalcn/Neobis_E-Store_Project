from django.urls import path
from .views import ListProduct, ListCategory, RetrieveProduct, RetrieveCategory

urlpatterns = [
    path('list-product/', ListProduct.as_view(), name='list-product'),
    path('list-category/', ListCategory.as_view(), name='list-category'),
    path('retrieve-product/<str:slug>/', RetrieveProduct.as_view(), name='retrieve-product'),
    path('retrieve-category/<str:slug>/', RetrieveCategory.as_view(), name='retrieve-category'),
]