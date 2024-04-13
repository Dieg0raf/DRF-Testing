# Django imports 
from django.contrib import admin
from django.urls import path, include

# Rest_Framework
from rest_framework import routers

# From App
from products.views import ProductViewSet

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/v2/', include(router.urls)),
]
