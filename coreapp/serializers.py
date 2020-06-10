from rest_framework import serializers
from coreapp.models import Employee, Salary


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'


class SalarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Salary
        fields = '__all__'
