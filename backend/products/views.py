# Rest_Framework imports
from rest_framework import generics, mixins 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets 

# Django imports
from django.shortcuts import get_object_or_404

# From Products app
from .models import Product
from .serializers import ProductSerializer
from api.mixins import StaffEditorPermissionMixin

# View Sets
class ProductViewSet(
    StaffEditorPermissionMixin,
    viewsets.ModelViewSet
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

# Class Based Views and 1 Function Based View (Does the same as the class views)
class ProductListCreateAPIView(
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission] # isn't need because of the StaffEditorPermissionMixin

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print(f'VALIDATED DATA: \n {serializer.validated_data}')
        # print(f"SERIALIZED ERRORS: {serializer.errors}")
        # email = serializer.validated_data.pop('email')
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

class ProductDetailAPIView(
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView,
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.content is None:
            instance.content = instance.title

class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        print(f'INSTANCE BEING DESTROYED: ({instance})')
        super().perform_destroy(instance)

class ProductMixinView(
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView,
    ):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.update(request, *args, **kwargs)
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.destroy(request, *args, **kwargs)

@api_view(['POST', 'GET', 'DELETE'])
def product_alt_view(request, pk=None, *args, **kwargs):
    print('IN PRODUCT ALT VIEW')
    method = request.method 
    # print(request.META['REMOTE_ADDR'])

    if method == 'GET':
        if pk != None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj).data
            return Response(data)
        
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
        # detail and list view

    if method == 'POST':
        if pk != None:
            obj = get_object_or_404(Product, pk=pk)

            serializer = ProductSerializer(instance=obj, data=request.data)
            if serializer.is_valid(raise_exception=True):
                instance = serializer.save()
                if instance.content is None:
                    instance.content = instance.title

                return Response(serializer.data)
            else:
                return Response({"invalid": "Product couldn't be updated"}, status=405)

        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)            

        return Response({"invalid" "not good data"}, status=400)
    
    if method == "DELETE":
        print(method)
        if pk != None:
            obj = get_object_or_404(Product, pk=pk)
            obj.delete()
            return Response(status=200)
        else:
            return Response({"invalid": "Product couldn't be updated"}, status=405)