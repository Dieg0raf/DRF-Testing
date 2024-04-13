from django.urls import path
from .views import (
    ProductDetailAPIView, 
    ProductListCreateAPIView, 
    product_alt_view, 
    ProductUpdateAPIView,
    ProductDestroyAPIView,
    ProductMixinView,
    )

urlpatterns = [
    path('<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('<int:pk>/update/', ProductUpdateAPIView.as_view(), name='product-edit'),
    path('<int:pk>/delete/', ProductDestroyAPIView.as_view()),
    path('', ProductListCreateAPIView.as_view(), name='product-list'),
]