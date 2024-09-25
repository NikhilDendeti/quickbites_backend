from typing import List

from qb_order.dtos import CategoryDTO


class GetCategoryPresenter:
    @staticmethod
    def get_categories_response(categories: List[CategoryDTO]):
        return {
            "categories": [
                {
                    "category_id": category.category_id,
                    "name": category.name,
                    "items": [
                        {
                            "item_id": item.item_id,
                            "name": item.name,
                            "description": item.description,
                            "item_image_url": item.item_image_url,
                            "is_veg": item.is_veg,
                            "price": item.price
                        } for item in category.items
                    ]
                } for category in categories
            ]
        }
