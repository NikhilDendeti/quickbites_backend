from typing import List
from decimal import Decimal
from datetime import datetime
from qb_order.dtos import UserOrderDTO, OrderItemDTO
from qb_order.models.items import FoodItem
from qb_order.models.orders import UserOrder, UserOrderItem
from django.db import transaction


class CreateOrUpdateOrderStorage:
    def get_user_order(self, user_id: str) -> UserOrder:
        """
        Retrieve an existing order for the user with status 'IN_PROGRESS'.
        """
        try:
            return UserOrder.objects.get(user_id=user_id, status='IN_PROGRESS')
        except UserOrder.DoesNotExist:
            return None

    @transaction.atomic
    def create_or_update_order(self, user_id: str, order_data: dict) -> UserOrderDTO:
        """
        Create or update a user order. If an order already exists with status 'IN_PROGRESS',
        it will be updated; otherwise, a new order is created.
        """
        # Step 1: Retrieve or create the user order
        order = self.get_user_order(user_id)
        if not order:
            order = UserOrder.objects.create(user_id=user_id, total_amount=Decimal(0))

        # Step 2: Clear existing items for the order to update with new ones
        UserOrderItem.objects.filter(order=order).delete()

        # Step 3: Add new items to the order and calculate the total amount
        total_amount = Decimal(0)
        items_dto = []

        for item_data in order_data.get('items', []):
            try:
                food_item = FoodItem.objects.get(item_id=item_data['item_id'])
            except FoodItem.DoesNotExist:
                continue  # Skip if item not found

            # Create new UserOrderItem entry
            user_order_item = UserOrderItem.objects.create(
                order=order,
                item=food_item,
                item_price=food_item.price
            )

            # Update total amount
            total_amount += food_item.price

            # Add to items DTO list
            items_dto.append(OrderItemDTO(
                item_id=str(food_item.item_id),
                count=1,
                total_amount=float(food_item.price)
            ))

        # Update the total amount of the order and save it
        order.total_amount = total_amount
        order.save()

        # Step 4: Prepare and return UserOrderDTO
        return UserOrderDTO(
            order_id=str(order.order_id),
            total_amount=float(order.total_amount),
            order_created_at=order.order_created_at.isoformat(),
            order_updated_at=order.order_updated_at.isoformat(),
            user_id=str(order.user_id),
            status=order.status,
            total_items_count=len(items_dto),
            items=items_dto
        )
