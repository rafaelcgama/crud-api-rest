from rest_framework import serializers
from core.models import User, Salary


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = '__all__'