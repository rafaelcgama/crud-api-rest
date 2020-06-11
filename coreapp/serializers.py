from django.db import models
from rest_framework import serializers
from coreapp.models import Employee, Salary
from djmoney.models.fields import MoneyField


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = '__all__'


class Calculations(models.Model):
    """Create a MoneyField datatype to be able to serialize"""
    amount = MoneyField(max_digits=7, decimal_places=2)


class CalculationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calculations
        fields = '__all__'
