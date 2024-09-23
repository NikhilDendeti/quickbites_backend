from rest_framework import serializers


class SigninRequestSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=150)


class SigninResponseSerializer(serializers.Serializer):
    access_token = serializers.CharField(max_length=150)
    refresh_token = serializers.CharField(max_length=150)
    user_id = serializers.CharField(max_length=150)
    expires_in = serializers.IntegerField()


class GetUserProfileDetailsResponseSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email=serializers.CharField(max_length=150)
    role=serializers.CharField(max_length=150)
    user_id=serializers.CharField(max_length=150)


class CreateUserRequestSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=150)


class CreateUserResponseSerializer(serializers.Serializer):
    access_token = serializers.CharField(max_length=150)
    refresh_token = serializers.CharField(max_length=150)
    user_id = serializers.CharField(max_length=150)
    expires_in = serializers.IntegerField()
