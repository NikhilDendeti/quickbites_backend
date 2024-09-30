from qb_order.dtos import UserOrderDTO
from qb_order.exceptions import InvalidUserIdException, ItemNotFoundException
from qb_order.models.items import FoodItem
from qb_order.models.orders import UserOrderItem, UserOrder


class UserOrderStorage:

    @staticmethod
    def create_user_order(order_data: dict):
        order = UserOrder.objects.create(
            user_id=order_data['user_id'],
            total_amount=order_data['total_amount'],
            status=order_data['status']
        )
        order.save()

        order_items = []
        for item_data in order_data['items']:
            try:
                food_item = FoodItem.objects.get(item_id=item_data['item_id'])
            except FoodItem.DoesNotExist:
                raise ItemNotFoundException(
                    f"Item with ID {item_data['item_id']} not found.")

            order_item = UserOrderItem.objects.create(
                order_id=order,
                item=food_item,
                item_price=item_data['total_amount'] / item_data['count'],
                count=item_data['count']
            )

            order_items.append(order_item)

        return order, order_items

    @staticmethod
    def get_user_order_by_user_id(user_id: str) -> list:
        try:
            user_orders = UserOrder.objects.filter(user_id=user_id)
        except UserOrder.DoesNotExist:
            raise InvalidUserIdException("No orders found for this user ID.")

        return [UserOrderStorage._get_user_order_dto_from_obj(order) for order
                in user_orders]

    @staticmethod
    def _get_user_order_dto_from_obj(order):
        return UserOrderDTO(
            order_id=str(order.order_id),
            total_amount=order.total_amount,
            status=order.status,
            order_created_at=order.order_created_at.isoformat(),
            order_updated_at=order.order_updated_at.isoformat()
        )

    @staticmethod
    def is_order_exists(order_id: str) -> bool:
        return UserOrder.objects.filter(order_id=order_id).exists()
