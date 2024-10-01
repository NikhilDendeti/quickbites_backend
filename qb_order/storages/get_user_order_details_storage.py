from typing import List

from qb_order.exceptions import OrderNotFoundException
from qb_order.models.orders import UserOrder, UserOrderItem
from qb_users.models import UserAccount


class UserOrderStorage:

    @staticmethod
    def is_valid_user(user_id: str) -> bool:

        return UserAccount.objects.filter(id=user_id).exists()

    @staticmethod
    def get_user_order_details(user_id: str) -> List[dict]:

        orders = UserOrder.objects.filter(user_id=user_id)

        if not orders.exists():
            raise OrderNotFoundException("No orders found for this user")

        order_items = UserOrderItem.objects.filter(
            order__in=orders).select_related('item')

        user_order_details = []
        for order in orders:
            items = [
                {
                    "item_id": str(order_item.item.item_id),
                    "count": 1,
                    "total_amount": str(order_item.item_price)
                }
                for order_item in order_items if order_item.order == order
            ]

            user_order_details.append({
                "order_id": str(order.order_id),
                "total_amount": str(order.total_amount),
                "order_created_at": order.order_created_at.isoformat(),
                "order_updated_at": order.order_updated_at.isoformat(),
                "user_id": str(order.user_id),
                "status": order.status,
                "total_items_count": len(items),
                "items": items
            })

        return user_order_details
