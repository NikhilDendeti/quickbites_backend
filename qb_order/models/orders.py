from django.db import models
import uuid

from qb_order.models.items import OrderStatus, FoodItem


class UserOrder(models.Model):
    order_id = models.UUIDField(primary_key=True, editable=False,
                                default=uuid.uuid4)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,
                                       default=0)
    order_created_at = models.DateTimeField(auto_now_add=True)
    order_updated_at = models.DateTimeField(auto_now=True)
    user_id = models.CharField(editable=False, max_length=150)
    status = models.CharField(max_length=150,
                              choices=OrderStatus.choices(),
                              default=OrderStatus.IN_PROGRESS.value)


class UserOrderItem(models.Model):
    order_id = models.ForeignKey(UserOrder, on_delete=models.CASCADE)
    user_order_item_id = models.UUIDField(primary_key=True, editable=False,
                                          default=uuid.uuid4)
    item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    item_price = models.DecimalField(max_digits=10, decimal_places=2,
                                     default=0)
