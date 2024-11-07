
import json
from typing import List
from django.http import HttpResponse
from qb_order.dtos import CategoryDTO

class GetCategoryPresenter:
    @staticmethod
    def get_categories_response(categories: List[CategoryDTO]) -> HttpResponse:
        response_data = {
            "categories": [category.to_dict() for category in categories]
        }
        return HttpResponse(
            content=json.dumps(response_data),
            status=200
        )

    @staticmethod
    def raise_no_categories_found_exception() -> HttpResponse:
        return HttpResponse(
            content=json.dumps({
                "message": "No categories found"
            }),
            status=404
        )

    @staticmethod
    def raise_specific_exception() -> HttpResponse:
        return HttpResponse(
            content=json.dumps({
                "message": "A specific error occurred while processing your request"
            }),
            status=400
        )

    @staticmethod
    def raise_unexpected_error_response(error_message: str) -> HttpResponse:
        return HttpResponse(
            content=json.dumps({
                "message": f"An unexpected error occurred: {error_message}"
            }),
            status=500
        )
