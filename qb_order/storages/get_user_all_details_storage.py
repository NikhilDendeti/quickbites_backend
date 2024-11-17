from typing import List, Tuple

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from qb_order.dtos import UserOrderDTO, OrderItemDTO
from qb_order.exceptions import NoOrdersFoundException
from qb_order.models.orders import UserOrder


class UserAllOrderStorage:
    @staticmethod
    def get_paginated_user_orders(
            user_id: str, page_number: int, page_size: int
    ) -> Tuple[List[UserOrderDTO], int]:
        orders = UserOrder.objects.filter(user_id=user_id).order_by(
            '-order_created_at')

        if not orders.exists():
            raise NoOrdersFoundException("No orders found for the user")

        paginator = Paginator(orders, page_size)

        try:
            page = paginator.page(page_number)
        except (EmptyPage, PageNotAnInteger):
            return [], paginator.num_pages
        orders_dto = [
            UserOrderDTO(
                order_id=order.order_id,
                total_amount=order.total_amount,
                order_created_at=order.order_created_at.isoformat(),
                order_updated_at=order.order_updated_at.isoformat() if order.order_updated_at else None,
                user_id=order.user_id,
                status=order.status,
                total_items_count=order.items.count(),
                items=[
                    OrderItemDTO(
                        item_id=item.item.item_id,
                        count=item.item.count,
                        total_amount=item.item_price
                    ) for item in order.items.all()
                ]
            ) for order in page
        ]

        return orders_dto, paginator.num_pages
