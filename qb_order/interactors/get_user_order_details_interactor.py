from qb_order.storages.get_user_order_details_storage import UserOrderStorage


class UserOrderInteractor:
    @staticmethod
    def create_user_order(user_id, amount_to_add):
        order = UserOrderStorage.create_or_update_user_order(user_id,
                                                             amount_to_add)
        return order

    @staticmethod
    def get_user_order_details(user_id, order_id):
        order_details = UserOrderStorage.get_user_order(user_id, order_id)
        return order_details
