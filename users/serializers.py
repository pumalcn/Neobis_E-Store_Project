from rest_framework import serializers
from django.contrib.auth.models import User

from product.models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id', 'address']


class CustomUserSerializer(serializers.ModelSerializer):
    user_info = UserInfoSerializer(source='userinfo', read_only=True)  # source взял из атрибута related_name

    class Meta:
        model = User
        fields = ['username', 'email', 'user_info']
