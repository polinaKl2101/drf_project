from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from education.serializers import PaymentsSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    payments = PaymentsSerializer(many=True, read_only=True, source='user')

    class Meta:
        model = User
        fields = '__all__'

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)