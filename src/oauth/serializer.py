from rest_framework import serializers
from . import models


class GoogleAuth(serializers.Serializer):
    """Сериализция данных от google"""
    email = serializers.EmailField()
    token = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AuthUser
        fields = ('avatar', 'country', 'city', 'bio', 'display_name')
