from enum import Enum

from django.db import models
import uuid


class OrderStatus(Enum):
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"

    @classmethod
    def choices(cls):
        return [(status.value, status.name) for status in cls]


class Category(models.Model):
    name = models.CharField(max_length=150)
    category_id = models.UUIDField(primary_key=True, editable=False,
                                   default=uuid.uuid4)

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    item_id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    is_veg = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    count=models.IntegerField(default=0)

    def __str__(self):
        return self.name


