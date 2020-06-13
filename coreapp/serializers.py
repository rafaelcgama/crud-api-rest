from django.db import models
from rest_framework import serializers
from coreapp.models import Employee, Salary
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MinMoneyValidator, MaxMoneyValidator


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = '__all__'


class MoneyFieldClass(models.Model):
    """Create a MoneyField datatype to be able to allow serialization"""
    amount = MoneyField(max_digits=8, decimal_places=2)


class CalculationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoneyFieldClass
        fields = '__all__'
