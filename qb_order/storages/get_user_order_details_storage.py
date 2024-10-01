from qb_order.dtos import UserOrderDTO, OrderItemDTO
from qb_order.models.orders import UserOrder, UserOrderItem


class UserOrderStorage:

    @staticmethod
    def get_user_order_details(user_id: str) -> UserOrderDTO:
        orders = UserOrder.objects.filter(user_id=user_id,
                                          status="IN_PROGRESS").order_by(
            '-order_created_at')

        if not orders.exists():
            return {"message": "No IN_PROGRESS orders found for this user"}

        recent_order = orders.first()

        order_items = UserOrderItem.objects.filter(
            order=recent_order).select_related('item')

        items = [
            OrderItemDTO(
                item_id=str(order_item.item.item_id),
                count=1,
                total_amount=float(order_item.item_price)
            )
            for order_item in order_items
        ]

        user_order_details = UserOrderDTO(
            order_id=str(recent_order.order_id),
            total_amount=float(recent_order.total_amount),
            order_created_at=recent_order.order_created_at.isoformat(),
            order_updated_at=recent_order.order_updated_at.isoformat(),
            user_id=str(recent_order.user_id),
            status=recent_order.status,
            total_items_count=len(items),
            items=items
        )

        return user_order_details
