from rest_framework import serializers
from orders.models import Order
from product.models import Product


class OrderSerializer(serializers.ModelSerializer):
    ORDER_STATUS_CHOICES = [
        ('processing', 'В процессе'),
        ('completed', 'Завершен'),
        ('canceled', 'Отменен'),
    ]

    ADDRESS_CHOICES = [
        ('default', 'Использовать адрес по умолчанию'),
        ('new', 'Использовать новый адрес'),
    ]

    client_products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    status = serializers.ChoiceField(choices=ORDER_STATUS_CHOICES)
    address_option = serializers.ChoiceField(choices=ADDRESS_CHOICES)
    new_address = serializers.CharField(max_length=255, required=False, allow_blank=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        new_address = validated_data.pop('new_address', '')
        order = super().create(validated_data)
        if order.address_option == 'new':
            order.new_address = new_address
            order.save()
        validated_data['new_address'] = new_address
        return order
