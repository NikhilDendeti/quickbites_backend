import json

from django.http import HttpResponse

from qb_order.dtos import UserOrderDTO


class GetUserOrderDetailsPresenter:
    @staticmethod
    def get_user_order_details_response(
            order_details: UserOrderDTO) -> HttpResponse:
        response_data = {
            "order_details": order_details.to_dict(),
            "message": "User order details retrieved successfully",
        }
        return HttpResponse(
            content=json.dumps(response_data),
            status=200
        )

    @staticmethod
    def raise_order_not_found_exception() -> HttpResponse:
        return HttpResponse(
            content=json.dumps({
                "message": "Order not found"
            }),
            status=404
        )

    @staticmethod
    def raise_invalid_user_id_exception() -> HttpResponse:
        return HttpResponse(
            content=json.dumps({
                "message": "Invalid User ID"
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
