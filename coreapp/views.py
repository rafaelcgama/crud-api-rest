from rest_framework.permissions import IsAuthenticated
from coreapp.models import Employee, Salary
from coreapp.serializers import EmployeeSerializer, SalarySerializer
from rest_framework.generics import GenericAPIView, RetrieveAPIView
# from rest_framework.mixins import (
#     CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin)
from rest_framework.viewsets import GenericViewSet, ModelViewSet


# class Emplo


class EmployeeViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class SalaryViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer

# class EmployeeList(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     permission_classes = (IsAuthenticated, )
#
#
# class SalaryList(generics.ListCreateAPIView):
#     queryset = Salary.objects.all()
#     serializer_class = SalarySerializer
#     permission_classes = (IsAuthenticated, )
