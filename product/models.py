from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Categories"

    def __str__(self) -> str:  # Аннотация типа str
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(unique=True)
    featured = models.BooleanField(default=False)
    thumbnail = models.URLField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    @property
    def related(self):
        return self.category.products.all().exclude(id=self.id)

    @property
    def rating(self):
        total_amount = self.reviews.all().count()
        if total_amount == 0:
            return 0
        rate = 0
        for i in self.reviews.all():
            rate += i.stars
        return rate / total_amount


class UserInfo(models.Model):
    user = models.OneToOneField(User, related_name='userinfo', on_delete=models.CASCADE)
    address = models.CharField(max_length=150)
    REQUIRED_FIELDS = ['address']

    def __str__(self):
        return self.user.username


class Review(models.Model):
    product_reviews = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField(max_length=1000)
    stars = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_author')

    def __str__(self):
        return self.review_text

