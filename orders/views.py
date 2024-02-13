from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination


from orders.models import Order
from orders.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-id')
    serializer_class = OrderSerializer
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        client = self.request.user
        serializer.save(client=client)
