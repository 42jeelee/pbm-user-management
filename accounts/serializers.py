from rest_framework import serializers

from userManagement.models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            nickname = validated_data['nickname'],
            name = validated_data['name'],
            profile = validated_data['profile'],
            password = validated_data['password'],
        )
        return user

    class Meta:
        model = User
        fields = ['email', 'nickname', 'name', 'profile', 'password']
