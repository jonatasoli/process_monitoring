from rest_framework import serializers
from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'url', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user."""

        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name'],
            url=validated_data['url']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class StatusProcessSerializer(serializers.ModelSerializer):
    """A serializer for process items."""

    class Meta:
        model = models.StatusProcess
        fields = ('id', 'user_profile', 'id_process', 'status_process')
        extra_kwargs = {'user_profile': {'read_only': True}}
