import json
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
from products.models import Product

# Rest_Framework imports
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Serializers
from products.serializers import ProductSerializer

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    
    return Response({"invalid": 'not good data'}, status=400)

    # instance = Product.objects.all().order_by("?").first()
    # data = {}
    # if instance:
    #     # data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])
    #     data = ProductSerializer(instance).data