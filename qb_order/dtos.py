# from dataclasses import dataclass
# from typing import List
# from uuid import UUID
#
# @dataclass
# class FoodItemDTO:
#     def __init__(self, item_id: UUID, name: str, description: str,
#                  item_image_url: str, is_veg: bool, price: float):
#         self.item_id = str(item_id)
#         self.name = name
#         self.description = description
#         self.item_image_url = item_image_url
#         self.is_veg = is_veg
#         self.price = price
#
#     def to_dict(self):
#         return {
#             "item_id": self.item_id,
#             "name": self.name,
#             "description": self.description,
#             "item_image_url": self.item_image_url,
#             "is_veg": self.is_veg,
#             "price": self.price,
#         }
#
#
# class CategoryDTO:
#     def __init__(self, category_id: UUID, name: str, items: List[FoodItemDTO]):
#         self.category_id = str(category_id)
#         self.name = name
#         self.items = items
#
#     def to_dict(self):
#         return {
#             "category_id": self.category_id,
#             "name": self.name,
#             "items": [item.to_dict() for item in self.items],
#         }
#
#
# class OrderItemDTO:
#     def __init__(self, item_id, count, total_amount):
#         self.item_id = item_id
#         self.count = count
#         self.total_amount = total_amount
#
#     def to_dict(self):
#         return {
#             "item_id": self.item_id,
#             "count": self.count,
#             "total_amount": self.total_amount
#         }
#
#
# class UserOrderDTO:
#     def __init__(self, order_id: UUID, total_amount: float,
#                  order_created_at: str,
#                  order_updated_at: str, user_id: UUID, status: str,
#                  total_items_count: int, items: List[OrderItemDTO]):
#         self.order_id = str(order_id)
#         self.total_amount = total_amount
#         self.order_created_at = order_created_at
#         self.order_updated_at = order_updated_at
#         self.user_id = str(user_id)
#         self.status = status
#         self.total_items_count = total_items_count
#         self.items = items
#
#     def to_dict(self):
#         return {
#             "order_id": self.order_id,
#             "total_amount": self.total_amount,
#             "order_created_at": self.order_created_at,
#             "order_updated_at": self.order_updated_at,
#             "user_id": self.user_id,
#             "status": self.status,
#             "total_items_count": self.total_items_count,
#             "items": [item.to_dict() for item in self.items]
#         }
#
#
# @dataclass
# class CategoryWithItemsDTO:
#     category: CategoryDTO
#     items: List[FoodItemDTO]
from dataclasses import dataclass
from typing import List
from uuid import UUID


@dataclass
class FoodItemDTO:
    item_id: str
    name: str
    description: str
    item_image_url: str
    is_veg: bool
    price: float

    def __init__(self, item_id: UUID, name: str, description: str,
                 item_image_url: str, is_veg: bool, price: float):
        self.item_id = str(item_id)
        self.name = name
        self.description = description
        self.item_image_url = item_image_url
        self.is_veg = is_veg
        self.price = price

    def to_dict(self):
        return {
            "item_id": self.item_id,
            "name": self.name,
            "description": self.description,
            "item_image_url": self.item_image_url,
            "is_veg": self.is_veg,
            "price": self.price
        }


@dataclass
class CategoryDTO:
    category_id: str
    name: str
    items: List[FoodItemDTO]

    def __init__(self, category_id: UUID, name: str, items: List[FoodItemDTO]):
        self.category_id = str(category_id)
        self.name = name
        self.items = items

    def to_dict(self):
        return {
            "category_id": self.category_id,
            "name": self.name,
            "items": [item.to_dict() for item in self.items]
        }


@dataclass
class OrderItemDTO:
    item_id: str
    count: int
    total_amount: float

    def __init__(self, item_id, count, total_amount):
        self.item_id = str(item_id)
        self.count = count
        self.total_amount = float(total_amount) if isinstance(total_amount, Decimal) else total_amount

    def to_dict(self):
        return {
            "item_id": self.item_id,
            "count": self.count,
            "total_amount": self.total_amount
        }


@dataclass
class UserOrderDTO:
    order_id: str
    total_amount: float
    order_created_at: str
    order_updated_at: str
    user_id: str
    status: str
    total_items_count: int
    items: List[OrderItemDTO]

    def __init__(self, order_id, total_amount, order_created_at, order_updated_at, user_id, status, total_items_count, items):
        self.order_id = str(order_id)
        self.total_amount = float(total_amount) if isinstance(total_amount, Decimal) else total_amount
        self.order_created_at = order_created_at
        self.order_updated_at = order_updated_at
        self.user_id = str(user_id)
        self.status = status
        self.total_items_count = total_items_count
        self.items = items

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "total_amount": self.total_amount,
            "order_created_at": self.order_created_at,
            "order_updated_at": self.order_updated_at,
            "user_id": self.user_id,
            "status": self.status,
            "total_items_count": self.total_items_count,
            "items": [item.to_dict() for item in self.items]
        }


@dataclass
class CategoryWithItemsDTO:
    category: CategoryDTO
    items: List[FoodItemDTO]


@dataclass
class UserProfileDTO:
    user_id: str
    username: str
    email: str
    role: str


@dataclass
class UserSigninDTO:
    username: str
    password: str


@dataclass
class TokenDTO:
    access_token: str
    refresh_token: str
    expires_in: str


@dataclass
class UserTokenDTO(TokenDTO):
    user_id: str


# Custom JSON Encoder to handle UUIDs
import json
from decimal import Decimal
from uuid import UUID

class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return str(obj)
        elif isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)


