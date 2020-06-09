from django.forms import ModelForm
from .models import User, Salary


class UserCreate(ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class SalaryCreate(ModelForm):
    class Meta:
        model = Salary
        fields = '__all__'
