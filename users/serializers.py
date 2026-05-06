from rest_framework import serializers
from .models import User
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_repeat = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'password', 'password_repeat']

    def validate(self, data):
        if data['password'] != data['password_repeat']:
            raise serializers.ValidationError("Пароли не совпадают")
        return data

    def create(self, validated_data):
        validated_data.pop('password_repeat')
        password = validated_data.pop('password')

        user = User(**validated_data)
        user.set_password(password)
        user.save()

        return user
