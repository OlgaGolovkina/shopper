from django.urls import path, include, re_path
from rest_framework import routers

from . import views
from shop.api.views import CartView

router = routers.DefaultRouter()
router.register('books', views.ProductAPIView)


urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^cart/$', CartView.as_view(), name='cart'),
]
