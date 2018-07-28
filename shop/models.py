from django.db import models
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

class Product(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=150)
    image = models.CharField(max_length=255)
    rating = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()


    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.ForeignKey(to=User, null=True, on_delete=models.CASCADE, related_name='cart_units')
    session = models.ForeignKey(to=Session, null=True, on_delete=models.CASCADE, related_name='cart_units')
    product = models.ForeignKey(to=Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return '{} unit(s) of {}'.format(self.quantity, self.product)

