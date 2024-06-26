from rest_framework import serializers
from .models import Category, Product, Review

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'title', 'content', 'rating', 'date_added', 'user_name']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'category', 'price', 'discount_price', 'stock',
            'date_modified', 'date_added', 'sku', 'image_url', 'is_active', 'rating',
            'num_reviews', 'reviews'
        ]
