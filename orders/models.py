from django.db import models
from django.contrib.auth.models import User
from product.models import Product


class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('processing', 'В процессе'),
        ('completed', 'Завершен'),
        ('canceled', 'Отменен'),
    ]
    ADDRESS_CHOICES = [
        ('default', 'Использовать адрес по умолчанию'),
        ('new', 'Использовать новый адрес'),
    ]
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    client_products = models.ManyToManyField(Product)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='processing')
    created_date = models.DateTimeField(auto_now_add=True)
    address_option = models.CharField(max_length=150, choices=ADDRESS_CHOICES, default='default')
    new_address = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f'Order #{self.id}'

    def save(self, *args, **kwargs):
        if self.address_option == 'default':
            self.address_option = self.client.userinfo.address
        super().save(*args, **kwargs)