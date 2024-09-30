from rest_framework import serializers


class ItemSerializer(serializers.Serializer):
    item_id = serializers.CharField(required=True)
    count = serializers.IntegerField(required=True)
    total_amount = serializers.FloatField(required=True)


class CreateUserOrderSerializer(serializers.Serializer):
    total_amount = serializers.FloatField(required=True)
    user_id = serializers.CharField(required=True)
    status = serializers.CharField(required=True)
    items = ItemSerializer(many=True, required=True)