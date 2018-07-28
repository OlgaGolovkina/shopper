from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from ..models import Product
from ..models import Cart

class ProductModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'url',
            'title',
            'author',
            'image',
            'rating',
            'description',
            'price',
        ]


class CartUnitSerializer(serializers.HyperlinkedModelSerializer):
    # sku = serializers.CharField(write_only=True)
    quantity = serializers.IntegerField(default=1, min_value=1)
    # product = UnitForOrderDetail(read_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'url', 'quantity', 'product')

    # def validate(self, data):
    #     sku = data['sku']
    #     quantity = data['quantity']
    # 
    #     try:
    #         unit = Unit.objects.get(sku=sku)
    #     except ObjectDoesNotExist:
    #         raise serializers.ValidationError('Unit does not exist')
    # 
    #     if unit.num_in_stock < quantity:
    #         raise serializers.ValidationError('There are not enough units in stock')
    # 
    #     return data

