from rest_framework import serializers


class ItemSerializer(serializers.Serializer):
    item_id = serializers.CharField(required=True)
    count = serializers.IntegerField(required=True)
    total_amount = serializers.FloatField(required=True)


class GetUserOrderDetailsSerializer(serializers.Serializer):
    order_id = serializers.CharField(required=True)
    total_amount = serializers.FloatField(required=True)
    order_created_at = serializers.DateTimeField(required=True)
    order_updated_at = serializers.DateTimeField(required=True)
    user_id = serializers.CharField(required=True)
    status = serializers.CharField(required=True)
    total_items_count = serializers.IntegerField(required=True)
    items = ItemSerializer(many=True, required=True)
