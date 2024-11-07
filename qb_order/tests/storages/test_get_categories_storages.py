import pytest
import uuid
from qb_order.models.items import Category, FoodItem
from qb_order.storages.get_categories_storages import GetCategoryStorage
from qb_order.exceptions import NoCategoriesFoundException

@pytest.mark.django_db
class TestGetCategoryStorage:

    def test_get_all_categories_with_items_success(self):
        # Arrange
        category_id = uuid.uuid4()
        category = Category.objects.create(category_id=category_id, name="Category 1")
        item1 = FoodItem.objects.create(
            item_id=uuid.uuid4(), name="Item 1", description="Description 1",
            item_image_url="http://image.url/item1.jpg", is_veg=True,
            price=100.0, category=category
        )
        item2 = FoodItem.objects.create(
            item_id=uuid.uuid4(), name="Item 2", description="Description 2",
            item_image_url="http://image.url/item2.jpg", is_veg=False,
            price=150.0, category=category
        )

        # Act
        result = GetCategoryStorage.get_all_categories_with_items()

        # Assert
        assert len(result) == 1
        assert str(result[0].category_id) == str(category.category_id)
        assert result[0].name == category.name
        assert len(result[0].items) == 2
        assert str(result[0].items[0].item_id) == str(item1.item_id)
        assert str(result[0].items[1].item_id) == str(item2.item_id)

    def test_get_all_categories_with_items_no_categories_found(self):
        # Act & Assert
        with pytest.raises(NoCategoriesFoundException, match="No categories found"):
            GetCategoryStorage.get_all_categories_with_items()

    def test_get_all_categories_with_items_category_without_items(self):
        # Arrange
        category_id = uuid.uuid4()
        category = Category.objects.create(category_id=category_id, name="Category 1")

        # Act
        result = GetCategoryStorage.get_all_categories_with_items()

        # Assert
        assert len(result) == 1
        assert str(result[0].category_id) == str(category.category_id)
        assert result[0].name == category.name
        assert len(result[0].items) == 0

    def test_get_all_categories_with_items_multiple_categories_with_items(self):
        # Arrange
        category_id1 = uuid.uuid4()
        category_id2 = uuid.uuid4()
        category1 = Category.objects.create(category_id=category_id1, name="Category 1")
        category2 = Category.objects.create(category_id=category_id2, name="Category 2")
        FoodItem.objects.create(
            item_id=uuid.uuid4(), name="Item 1", description="Description 1",
            item_image_url="http://image.url/item1.jpg", is_veg=True,
            price=100.0, category=category1
        )
        FoodItem.objects.create(
            item_id=uuid.uuid4(), name="Item 2", description="Description 2",
            item_image_url="http://image.url/item2.jpg", is_veg=False,
            price=150.0, category=category1
        )
        FoodItem.objects.create(
            item_id=uuid.uuid4(), name="Item 3", description="Description 3",
            item_image_url="http://image.url/item3.jpg", is_veg=True,
            price=200.0, category=category2
        )

        # Act
        result = GetCategoryStorage.get_all_categories_with_items()

        # Assert
        assert len(result) == 2
        assert str(result[0].category_id) == str(category1.category_id)
        assert len(result[0].items) == 2
        assert str(result[1].category_id) == str(category2.category_id)
        assert len(result[1].items) == 1
