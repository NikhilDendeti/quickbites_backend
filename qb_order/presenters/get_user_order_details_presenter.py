import json
from typing import List
from django.http import HttpResponse


class GetUserOrderDetailsPresenter:
    @staticmethod
    def get_user_order_details_response(
            order_details: List[dict]) -> HttpResponse:
        response_data = {
            "order_details": order_details,
            "message": "User order details retrieved successfully",
        }
        return HttpResponse(
            status=200,
            content=json.dumps(response_data)
        )

    @staticmethod
    def raise_order_not_found_exception() -> HttpResponse:
        return HttpResponse(
            status=404,
            content=json.dumps({
                "message": "Order not found"
            })
        )

    @staticmethod
    def raise_invalid_user_id_exception() -> HttpResponse:
        return HttpResponse(
            status=400,
            content=json.dumps({
                "message": "Invalid User ID"
            })
        )

    @staticmethod
    def raise_unexpected_error_response(error_message: str) -> HttpResponse:
        return HttpResponse(
            status=500,
            content=json.dumps({
                "message": f"An unexpected error occurred: {error_message}"
            })
        )
