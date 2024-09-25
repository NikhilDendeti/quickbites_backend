from django.contrib import admin

from qb_order.models.items import Category, FoodItem
from qb_order.models.orders import UserOrderItem, UserOrder

admin.site.register(UserOrder)
admin.site.register(UserOrderItem)
admin.site.register(Category)
admin.site.register(FoodItem)
