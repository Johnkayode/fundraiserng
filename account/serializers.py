from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login

from rest_framework import serializers, generics, status
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response

from .exceptions import CustomException
from .models import CustomUser

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            "uid",
            "email",
            "first_name",
            "last_name",
            "password",

            "date_joined",
            "last_login",
            "is_active",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "date_joined": {"read_only": True},
            "last_login": {"read_only": True},
            "is_active": {"read_only": True},

        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class ConfirmAccountSerializer(serializers.Serializer):
    confirmation_code = serializers.IntegerField(required=True)

class UserLoginSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)

        if user is None:
            raise CustomException({'detail':'Email or password does not exist'})
        elif not user.is_active:
            raise CustomException({'detail':'User account has not been confirmed'})
        

        payload = JWT_PAYLOAD_HANDLER(user)
        jwt_token = JWT_ENCODE_HANDLER(payload)
        update_last_login(None, user)

        return {
            'email': user.email,
            'token': jwt_token
        }

class ChangePasswordSerializer(serializers.Serializer):

    password = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)
    old_password = serializers.CharField(required=True, write_only=True)


    def validate(self, attrs):
        user = self.context['request'].user

        if not user.check_password(attrs['old_password']):
            raise CustomException({'detail':'Old password is incorrect'})

        if attrs['password'] != attrs['password2']:
            raise CustomException({'detail':'Passwords do not match'})

        return attrs

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        print('Eniola na sage')
        return instance

class UserDashboardSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            "uid",
            "email",
            "first_name",
            "last_name",
            "date_joined",
        )

        extra_kwargs = {
            "uid": {"read_only": True},
            "date_joined": {"read_only": True},
        }

        
        