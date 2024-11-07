import uuid

import pytest

from qb_order.dtos import UserOrderDTO
from qb_order.models.items import FoodItem, Category
from qb_order.models.orders import UserOrder, UserOrderItem
from qb_order.storages.get_user_order_details_storage import UserOrderStorage


@pytest.mark.django_db
class TestUserOrderStorage:

    def test_get_user_order_details_with_existing_order(self):
        # Arrange
        user_id = uuid.uuid4()
        order = UserOrder.objects.create(
            order_id=uuid.uuid4(),
            user_id=user_id,
            status="IN_PROGRESS",
            total_amount=150.0
        )

        category = Category.objects.create(
            category_id=uuid.uuid4(),
            name="Category 1"
        )

        food_item1 = FoodItem.objects.create(
            item_id=uuid.uuid4(),
            name="Item 1",
            description="Description 1",
            item_image_url="http://image.url/item1.jpg",
            is_veg=True,
            price=75.0,
            category=category
        )
        food_item2 = FoodItem.objects.create(
            item_id=uuid.uuid4(),
            name="Item 2",
            description="Description 2",
            item_image_url="http://image.url/item2.jpg",
            is_veg=False,
            price=75.0,
            category=category
        )

        UserOrderItem.objects.create(
            order=order,
            item=food_item1,
            item_price=75.0
        )
        UserOrderItem.objects.create(
            order=order,
            item=food_item2,
            item_price=75.0
        )

        storage = UserOrderStorage()

        # Act
        result = storage.get_user_order_details(user_id=user_id)

        # Assert
        assert isinstance(result, UserOrderDTO)
        assert result.order_id == str(order.order_id)
        assert result.total_amount == 150.0
        assert len(result.items) == 2

    def test_get_user_order_details_no_order_found(self):
        # Arrange
        user_id = uuid.uuid4()
        storage = UserOrderStorage()

        # Act
        result = storage.get_user_order_details(user_id=user_id)

        # Assert
        assert result is None

    def test_get_user_order_details_only_completed_orders(self):
        # Arrange
        user_id = uuid.uuid4()
        UserOrder.objects.create(
            order_id=uuid.uuid4(),
            user_id=user_id,
            status="COMPLETED",
            total_amount=150.0
        )

        storage = UserOrderStorage()

        # Act
        result = storage.get_user_order_details(user_id=user_id)

        # Assert
        assert result is None
