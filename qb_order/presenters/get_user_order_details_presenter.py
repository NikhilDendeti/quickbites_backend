from rest_framework.response import Response
from rest_framework import status


class UserOrderPresenter:
    @staticmethod
    def present_create(order):
        response_data = {
            "order_id": str(order.order_id),
            "total_amount": str(order.total_amount),
            "order_created_at": order.order_created_at.strftime('%Y-%m-%d %H:%M:%S'),
            "order_updated_at": order.order_updated_at.strftime('%Y-%m-%d %H:%M:%S'),
            "user_id": order.user_id,
            "status": order.status,
        }
        return Response(response_data, status=status.HTTP_201_CREATED)

    @staticmethod
    def present_get(order_details):
        if order_details is None:
            return Response({"detail": "Order not found"},
                            status=status.HTTP_404_NOT_FOUND)

        return Response(order_details, status=status.HTTP_200_OK)
