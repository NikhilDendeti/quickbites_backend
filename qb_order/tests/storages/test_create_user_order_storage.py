import uuid

import pytest

from qb_order.models.items import Category, FoodItem
from qb_order.storages.create_user_order_storage import \
    CreateOrUpdateOrderStorage


@pytest.mark.django_db
class TestCreateOrUpdateOrderStorage:

    def test_create_order_success(self):
        # Arrange
        user_id = "user123"

        # Create a category first
        category = Category.objects.create(
            category_id=uuid.uuid4(),
            name="Fast Food"
        )

        # Create food items linked to the category
        food_item1 = FoodItem.objects.create(
            item_id=uuid.uuid4(),
            name="Pizza",
            description="Delicious pizza",
            item_image_url="http://image.url/pizza.jpg",
            is_veg=True,
            price=100.0,
            category=category
        )
        food_item2 = FoodItem.objects.create(
            item_id=uuid.uuid4(),
            name="Burger",
            description="Tasty burger",
            item_image_url="http://image.url/burger.jpg",
            is_veg=False,
            price=150.0,
            category=category
        )

        order_data = {
            "items": [
                {"item_id": str(food_item1.item_id)},
                {"item_id": str(food_item2.item_id)}
            ]
        }

        # Act
        storage = CreateOrUpdateOrderStorage()
        result = storage.create_or_update_order(user_id, order_data)

        # Assert
        assert result.total_amount == 250.0
        assert len(result.items) == 2
        assert result.items[0].item_id == str(food_item1.item_id)
        assert result.items[1].item_id == str(food_item2.item_id)

    def test_no_items_provided(self):
        user_id = "user123"
        storage = CreateOrUpdateOrderStorage()
        result = storage.create_or_update_order(user_id, {"items": []})

        assert result.total_items_count == 0
        assert result.total_amount == 0

    def test_item_not_found(self):
        user_id = "user123"
        order_data = {"items": [{"item_id": "non_existent_item"}]}

        storage = CreateOrUpdateOrderStorage()
        result = storage.create_or_update_order(user_id, order_data)

        assert result.total_amount == 0
        assert result.total_items_count == 0
