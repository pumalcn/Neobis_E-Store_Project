from rest_framework import generics, viewsets
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Product, Category, Review
from .serializers import ProductSerializer, CategorySerializer, RetrieveProductSerializer, RetrieveCategorySerializer, \
    ReviewSerializer


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


class CreateProduct(generics.CreateAPIView):
    permission_classes = [permissions.IsAdminUser, ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UpdateProduct(generics.UpdateAPIView):
    permission_classes = [permissions.IsAdminUser, ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DestroyProduct(generics.DestroyAPIView):
    permission_classes = [permissions.IsAdminUser, ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CreateCategory(generics.CreateAPIView):
    permission_classes = [permissions.IsAdminUser, ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UpdateCategory(generics.UpdateAPIView):
    permission_classes = [permissions.IsAdminUser, ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DestroyCategory(generics.DestroyAPIView):
    permission_classes = [permissions.IsAdminUser, ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('-id')
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
