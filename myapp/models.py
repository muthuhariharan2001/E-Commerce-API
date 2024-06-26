from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock = models.IntegerField()
    date_modified = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)
    sku = models.CharField(max_length=50, unique=True)
    image_url = models.URLField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    num_reviews = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user_name} - {self.product.name}"
