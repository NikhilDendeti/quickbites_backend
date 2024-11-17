from typing import List

from qb_order.dtos import CategoryDTO, FoodItemDTO
from qb_order.exceptions import \
    NoCategoriesFoundException
from qb_order.models.items import Category, FoodItem


class GetCategoryStorage:
    @staticmethod
    def get_all_categories_with_items() -> List[CategoryDTO]:
        categories = Category.objects.all()

        if not categories.exists():
            raise NoCategoriesFoundException("No categories found")

        categories_dto = []

        for category in categories:
            items = FoodItem.objects.filter(category=category)
            items_dto = [
                FoodItemDTO(
                    item_id=item.item_id,
                    name=item.name,
                    description=item.description,
                    item_image_url=item.item_image_url,
                    is_veg=item.is_veg,
                    price=float(item.price)
                ) for item in items
            ]

            categories_dto.append(CategoryDTO(
                category_id=category.category_id,
                name=category.name,
                items=items_dto
            ))

        return categories_dto
