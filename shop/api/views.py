from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.sessions.models import Session

from ..models import Product, Cart
from .serializers import ProductModelSerializer, CartUnitSerializer


class ProductAPIView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


class CartView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        if not bool(request.user.is_anonymous):
            cart_units = request.user.cart_units.all()
        else:
            if request.session.session_key is None:
                request.session.save()

            cart_units = Session.objects.get(session_key=request.session.session_key).cart_units.all()

        return Response(CartUnitSerializer(cart_units, many=True).data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CartUnitSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        # product = Product.objects.get(sku=data['sku'])
        product = Product.objects.get()

        cart_unit_data = {
            'product': product,
            'quantity': quantity,
            'user': None,
            'session': None
        }

        if not bool(request.user.is_anonymous):
            cart_unit_data['user'] = request.user
        else:
            if request.session.session_key is None:
                request.session.save()

            cart_unit_data['session'] = Session.objects.get(session_key=request.session.session_key)

        cart_unit = Cart.objects.filter(**cart_unit_data).first()

        if cart_unit is None:
            cart_unit = Cart(**cart_unit_data)

        cart_unit.quantity = data['quantity']
        cart_unit.save()

        return Response(status=status.HTTP_201_CREATED)
