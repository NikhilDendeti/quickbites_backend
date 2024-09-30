import json

from django.http import HttpResponse


class CreateUserOrderPresenter:

    @staticmethod
    def present_order_creation_success(order_data: dict):
        response_data = {
            "order_id": order_data["order_id"],
            "total_amount": order_data["total_amount"],
            "status": order_data["status"],
            "total_items_count": len(order_data["items"]),
            "items": order_data["items"]
        }
        return HttpResponse(status=200, content=json.dumps(response_data))

    @staticmethod
    def present_order_creation_failure(error_message: str):
        return HttpResponse(status=400,
                            content=json.dumps({"errors": error_message}))

    @staticmethod
    def present_invalid_order_data(validation_errors: dict):
        return HttpResponse(
            status=400,
            content=json.dumps({
                "error": "Invalid Data",
                "details": validation_errors
            })
        )
