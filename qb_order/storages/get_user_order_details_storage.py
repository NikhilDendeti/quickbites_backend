from qb_order.exceptions import ObjectDoesNotExist
from qb_order.models.items import OrderStatus
from qb_order.models.orders import UserOrder, UserOrderItem


class UserOrderStorage:
    @staticmethod
    def create_or_update_user_order(user_id, amount_to_add):
        try:
            order = UserOrder.objects.get(user_id=user_id,
                                          status=OrderStatus.IN_PROGRESS.value)
            order.total_amount += amount_to_add
            order.save()
            return order
        except ObjectDoesNotExist:

            order = UserOrder.objects.create(user_id=user_id,
                                             total_amount=amount_to_add,
                                             status=OrderStatus.IN_PROGRESS.value)
            return order

    @staticmethod
    def get_user_order(user_id, order_id):
        try:
            order = UserOrder.objects.get(order_id=order_id, user_id=user_id)
            order_items = UserOrderItem.objects.filter(order_id=order)
            items_data = [
                {
                    "item_id": str(item.item.item_id),
                    "count": item.count,
                    "total_amount": str(item.total_amount),
                }
                for item in order_items
            ]
            return {
                "order_id": str(order.order_id),
                "total_amount": str(order.total_amount),
                "order_created_at": order.order_created_at.isoformat(),
                "order_updated_at": order.order_updated_at.isoformat(),
                "user_id": order.user_id,
                "status": order.status,
                "total_items_count": len(items_data),
                "items": items_data,
            }
        except ObjectDoesNotExist:
            return None
