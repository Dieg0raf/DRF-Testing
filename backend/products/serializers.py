from rest_framework import serializers
from rest_framework.reverse import reverse

from .validators import validate_title
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-edit',
        lookup_field = 'pk',
    )
    title = serializers.CharField(validators=[validate_title])
    name = serializers.CharField(source='title', read_only=True)
    email = serializers.EmailField(write_only=True)
    class Meta:
        model = Product
        fields = [
            'url',
            'edit_url',
            'email',
            'pk',
            'name',
            'title',
            'content',
            'price',
            'sale_price',
            'discount',
        ]

    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name.")

    #     return value
        

    # def create(self, validated_data):
    #     # email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     # print(email, obj)
    #     return obj

    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email')
    #     return 
        

    def get_edit_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)
        # return f'/api/products/{obj.pk}/'
        
    def get_discount(self, obj):
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()