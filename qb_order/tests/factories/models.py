import uuid
from datetime import datetime
from decimal import Decimal
import factory
from qb_order.models.items import FoodItem, Category
from qb_order.models.orders import UserOrder, UserOrderItem


class UserOrderFacatory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserOrder

    order_id = factory.LazyFunction(uuid.uuid4)
    total_amount = Decimal('100.00')
    order_created_at = datetime.now()
    order_updated_at = datetime.now()
    user_id = factory.LazyFunction(uuid.uuid4)
    status = 'IN_PROGRESS'


class UserOrderItemFacatory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserOrderItem

    user_order_item_id = factory.LazyFunction(uuid.uuid4)
    item_price = Decimal('100.00')
    item = factory.LazyFunction(uuid.uuid4)
    order_id = factory.LazyFunction(uuid.uuid4)


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: f'Category {n}')
    category_id = factory.LazyFunction(uuid.uuid4)


class FoodItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FoodItem

    item_id = factory.LazyFunction(uuid.uuid4)
    name = factory.Sequence(lambda n: f'FoodItem {n}')
    price = Decimal('100.00')
    description = 'FoodItem Description'
    item_image_url = 'https://example.com/item_image.jpg'
    is_veg = True
    is_available = True
    category = factory.SubFactory(CategoryFactory)
