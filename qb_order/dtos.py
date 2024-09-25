from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class FoodItemDTO:
    item_id: str
    name: str
    description: str
    item_image_url: str
    is_veg: bool
    price: float


@dataclass
class CategoryDTO:
    category_id: str
    name: str
    items: List[FoodItemDTO]


@dataclass
class OrderItemDTO:
    item_id: str
    count: int
    total_amount: float


@dataclass
class UserOrderDTO:
    order_id: str
    total_amount: float
    order_created_at: datetime
    order_updated_at: datetime
    user_id: str
    status: str
    total_items_count: int
    items: List[OrderItemDTO]
