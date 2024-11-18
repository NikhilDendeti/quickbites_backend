from django.urls import path

from qb_order.views.create_user_order import create_or_update_user_order
from qb_order.views.get_categories import get_categories
from qb_order.views.get_user_all_details import get_user_orders
from qb_order.views.get_user_order_details import get_user_order_details

urlpatterns = [
    path('get/categories/', get_categories),
    path('get/user/orders/details/', get_user_order_details),
    path('get/user/all/orders/', get_user_orders),
    path('create/user/order/', create_or_update_user_order)

]
