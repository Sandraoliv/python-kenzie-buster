from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(max_length=127)
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True, max_length=120)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(default=None)
    is_employee = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(default=False, read_only=True)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("username already taken.")
        return value
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("email already registered.")
        return value

    def create(self, validated_data: dict) -> User:
        if validated_data["is_employee"]:
            return User.objects.create_superuser(**validated_data)  
        return User.objects.create_user(**validated_data) 

    class LoginSerializer(serializers.Serializer):
        username = serializers.CharField(max_length=50, write_only=True)
        password = serializers.CharField(max_length=120, write_only=True)   