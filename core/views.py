from rest_framework import generics
from .models import User, Salary
from api.serializers import UserSerializer, SalarySerializer


# Create your views here.
# class UserList(ListView, CreateView, UpdateView, DeleteView):
#     model = User
#     fields = ['cpf', 'name', 'dob']
#
#     def create
#
# class UserList(ListView):
#     model = User
#     template_name = 'user_list.html'
#
#
# class SalaryList(ListView):
#     model = Salary
#     template_name = 'salary_list.html'
class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SalaryAPIView(generics.ListAPIView):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer

