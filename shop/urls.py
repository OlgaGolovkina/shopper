from django.urls import path

from .views import ShopPage


urlpatterns = [
    path('', ShopPage.as_view(), name='shop'),
]
