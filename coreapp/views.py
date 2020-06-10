from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics
from coreapp.models import Employee, Salary
from coreapp.serializers import EmployeeSerializer, SalarySerializer
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin)
from rest_framework.viewsets import GenericViewSet


class EmployeeViewSet(GenericViewSet,
                      CreateModelMixin,
                      RetrieveModelMixin,
                      UpdateModelMixin,
                      ListModelMixin):

    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class SalaryViewSet(GenericViewSet,
                    CreateModelMixin,
                    RetrieveModelMixin,
                    UpdateModelMixin,
                    ListModelMixin):

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
