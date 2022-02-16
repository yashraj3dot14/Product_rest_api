from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name= 'api:product-detail')
    class Meta:
        model = Product
        fields = '__all__'