from django.db.models import Avg
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from coreapp.models import Employee, Salary
from coreapp.serializers import EmployeeSerializer, SalarySerializer, MoneySerializer


class EmployeeViewSet(ModelViewSet):
    """"Creates Employees CRUD operations and views"""
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class SalaryViewSet(ModelViewSet):
    """"Creates Employees CRUD operations and views"""
    permission_classes = [IsAuthenticated]
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer


class CalculationsView(APIView):
    """"Calculates extra operations and view them"""
    permission_classes = [IsAuthenticated]
    serializer_class = MoneySerializer

    def get(self, request):
        queryset = Salary.objects.all()
        min_ = queryset.order_by('salary').first()
        max_ = queryset.order_by('salary').last()
        avg_salary = queryset.aggregate(Avg('salary'))['salary__avg']
        avg_deduction = queryset.aggregate(Avg('deduction'))['deduction__avg']
        content = {
            'Menor salários': str(min_.salary),
            'Maior salários': str(max_.salary),
            'Média dos salários': "R${:,.2f}".format(avg_salary),
            'Média dos descontos': "R${:,.2f}".format(avg_deduction)
        }

        return Response(content)
