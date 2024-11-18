from django.http import JsonResponse

from qb_order.dtos import UserOrderDTO


class CreateOrUpdateOrderPresenter:
    @staticmethod
    def get_order_response(order: UserOrderDTO) -> JsonResponse:
        return JsonResponse(order.to_dict(), status=200)

    @staticmethod
    def raise_order_not_found_exception() -> JsonResponse:
        return JsonResponse({"message": "Order not found"}, status=404)

    @staticmethod
    def raise_specific_exception() -> JsonResponse:
        return JsonResponse({"message": "A specific error occurred"},
                            status=400)

    @staticmethod
    def raise_unexpected_error_response(error_message: str) -> JsonResponse:
        return JsonResponse({"message": f"Unexpected error: {error_message}"},
                            status=500)
