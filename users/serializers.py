from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    otp_code = serializers.CharField(required=False)


    class Meta:
        model = User
        fields = ['phone_number', 'otp_code']
