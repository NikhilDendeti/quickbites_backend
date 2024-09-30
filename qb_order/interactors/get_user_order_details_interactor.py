from rest_framework.exceptions import ValidationError

from qb_order.serializers import CreateUserOrderSerializer


class CreateUserOrderInteractor:
    def __init__(self, storage):
        self.storage = storage

    def execute(self, request_body: dict):
        serializer = CreateUserOrderSerializer(data=request_body)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)

        order_data = serializer.validated_data
        total_items_count = len(order_data['items'])
        total_amount = sum(
            item['total_amount'] for item in order_data['items'])

        order, order_items = self.storage.create_user_order(
            order_data=order_data)

        order_dict = {
            "order_id": str(order.order_id),
            "total_amount": order.total_amount,
            "status": order.status,
            "order_created_at": order.order_created_at,
            "order_updated_at": order.order_updated_at,
        }

        order_items_dict = [
            {
                "user_order_item_id": str(item.user_order_item_id),
                "item_id": str(item.item.item_id),
                "item_price": item.item_price,
                "count": item.count
            }
            for item in order_items
        ]

        return {
            "order_id": order_dict['order_id'],
            "total_amount": total_amount,
            "status": order_dict['status'],
            "order_created_at": order_dict['order_created_at'],
            "order_updated_at": order_dict['order_updated_at'],
            "total_items_count": total_items_count,
            "items": order_items_dict
        }
