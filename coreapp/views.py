from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView

from coreapp.models import Employee, Salary
from django.db.models import Avg
from rest_framework.decorators import action, api_view
from coreapp.serializers import EmployeeSerializer, SalarySerializer
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet


def get_url(data):
    serializer = SalarySerializer(data=data)
    if serializer.is_valid():
        return Response(serializer.data)
    else:
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class EmployeeViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class SalaryViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    renderer_classes = (JSONRenderer,)

    """"A média dos salários
        - A média dos descontos
        - O maior salário
        - O menor salário"""

    # def salary_max(self):
    #     queryset = Salary.objects.all()
    #     max_ = queryset.order_by('salary').first()
    #     content = {'Média dos salários': max_}
    #     return Response(content)

    # @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    # def salary_min(self):
    #     queryset = Salary.objects.all()
    #     min_ = queryset.order_by('salary').last()
    #     return get_url(min_)
    #
    # @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    # def salary_avg(self):
    #     queryset = Salary.objects.all()
    #     avg = queryset.aggregate(Avg('salary'))
    #     return get_url(avg)
    #
    # @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    # def deduction_avg(self):
    #     queryset = Salary.objects.all()
    #     avg = queryset.aggregate(Avg('deduction'))
    #     return get_url(avg)


class SalaryMaxView(APIView):
    """
    A view that returns the count of active users.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = SalarySerializer

    def get(self, request):
        queryset = Salary.objects.all()
        min_ = queryset.order_by('salary').last()
        max_ = queryset.order_by('salary').first()
        avg_salary = queryset.aggregate(Avg('salary'))
        avg_descontos = queryset.aggregate(Avg('deduction'))
        content = {'Menor salários': min_,
                   'Maior salários': max_,
                   'Média dos salários': avg_salary,
                   'Média dos descontos': avg_descontos}
        serializer = SalarySerializer(data=content)
        return Response(serializer.data)

