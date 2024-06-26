from django.urls import path
from .views import CategoryListCreate, ProductListCreate, ReviewListCreate, ProductDetail

urlpatterns = [
    path('api/categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('api/products/', ProductListCreate.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('api/reviews/', ReviewListCreate.as_view(), name='review-list-create'),
]
