from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
