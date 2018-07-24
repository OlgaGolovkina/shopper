from rest_framework import generics

from ..models import Product
from .serializers import ProductModelSerializer


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductModelSerializer

    def get_queryset(self):
        return Product.objects.all()
