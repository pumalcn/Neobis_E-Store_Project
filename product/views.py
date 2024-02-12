from rest_framework import generics
from rest_framework import permissions
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer, RetrieveProductSerializer, RetrieveCategorySerializer


class ListProduct(generics.ListAPIView):
    permission_classes = [permissions.AllowAny, ]
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.order_by('-id')


class ListCategory(generics.ListAPIView):
    permission_classes = [permissions.AllowAny, ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RetrieveProduct(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny, ]
    queryset = Product.objects.all()
    serializer_class = RetrieveProductSerializer
    lookup_field = "slug"


class RetrieveCategory(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny, ]
    queryset = Category.objects.all()
    serializer_class = RetrieveCategorySerializer
    lookup_field = "slug"
