import json

from django.http import HttpResponse


class GetUserOrdersPresenter:
    @staticmethod
    def get_user_orders_response(orders, total_pages):
        response_data = {
            "orders": [order.to_dict() for order in orders],
            "total_pages": total_pages,
            "message": "User orders retrieved successfully" if orders else "No orders found"
        }
        return HttpResponse(
            content=json.dumps(response_data),
            status=200 if orders else 404
        )

    @staticmethod
    def raise_order_not_found_exception() -> HttpResponse:
        response_data = {"message": "No orders found"}
        return HttpResponse(
            content=json.dumps(response_data),
            status=404
        )

    @staticmethod
    def raise_unexpected_error_response(error_message: str) -> HttpResponse:
        response_data = {
            "message": f"An unexpected error occurred: {error_message}"}
        return HttpResponse(
            content=json.dumps(response_data),
            status=500
        )
