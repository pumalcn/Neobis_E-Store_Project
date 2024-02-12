from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):  # Теперь категория отображается с тремя поля, а не просто id
        context = super().to_representation(instance)
        context['category'] = {"id": instance.category.id, "title": instance.category.title, "slug": instance.category.slug}
        return context


class RetrieveProductSerializer(serializers.ModelSerializer):
    related_products = serializers.SerializerMethodField(method_name='get_related_products')

    class Meta:
        model = Product
        fields = (
            "id",
            "category",
            "title",
            "slug",
            "featured",
            "price",
            "thumbnail",
            "description",
            "created_date",
            "updated_date",
            "related_products",
        )

    def to_representation(self, instance):  # Теперь категория отображается с тремя поля, а не просто id
        context = super().to_representation(instance)
        context['category'] = {"id": instance.category.id, "title": instance.category.title, "slug": instance.category.slug}
        return context

    def get_related_products(self, obj):
        return ProductSerializer(obj.related, many=True).data


class RetrieveCategorySerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField(method_name='get_products')

    class Meta:
        model = Category
        fields = (
            "id",
            "title",
            "slug",
            "featured",
            "products",
            "created_date",
        )

    def get_products(self, obj):
        return ProductSerializer(obj.products.all(), many=True).data
