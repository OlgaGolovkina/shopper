from rest_framework import serializers

from ..models import Product


class ProductModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'url',
            'title',
            'description',
            'price',
        ]
