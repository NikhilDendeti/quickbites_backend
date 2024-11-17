import uuid

import pytest

from qb_order.exceptions import NoOrdersFoundException
from qb_order.models.items import Category, FoodItem
from qb_order.models.orders import UserOrder, UserOrderItem
from qb_order.storages.get_user_all_details_storage import UserAllOrderStorage


@pytest.mark.django_db
class TestUserAllOrderStorage:

    def test_get_paginated_user_orders_success(self):
        # Arrange
        user_id = "27a00ec7-46f5-4e62-8fca-17ab98c004c9"

        # Create a Category
        category = Category.objects.create(
            category_id=uuid.uuid4(),
            name="Fast Food"
        )

        # Create an Order
        order = UserOrder.objects.create(
            order_id=uuid.uuid4(),
            total_amount=200.0,
            user_id=user_id,
            status="COMPLETED"
        )

        # Create a FoodItem associated with the Category
        food_item = FoodItem.objects.create(
            item_id=uuid.uuid4(),
            name="Burger",
            description="Delicious burger",
            item_image_url="http://example.com/burger.jpg",
            is_veg=True,
            price=50.0,
            category=category,  # Ensure category is associated
            count=10
        )

        # Create a UserOrderItem linked to the FoodItem
        UserOrderItem.objects.create(
            order=order,
            item=food_item,
            item_price=50.0
        )

        # Act
        result, total_pages = UserAllOrderStorage.get_paginated_user_orders(
            user_id=user_id, page_number=1, page_size=5
        )

        # Assert
        assert len(result) == 1
        assert total_pages == 1
        assert result[0].user_id == user_id
        assert result[0].total_amount == 200.0
        assert len(result[0].items) == 1
        assert result[0].items[0].item_id == str(food_item.item_id)
        assert result[0].items[0].total_amount == 50.0

    def test_get_paginated_user_orders_no_orders_found(self):
        # Act & Assert
        with pytest.raises(NoOrdersFoundException,
                           match="No orders found for the user"):
            UserAllOrderStorage.get_paginated_user_orders(
                user_id="nonexistent_user", page_number=1, page_size=5
            )
