from django.db import models
from djmoney.models.fields import MoneyField
from django.core.validators import MinLengthValidator


# Create your models here.
class Employee(models.Model):
    """Creates Employee table"""
    cpf = models.CharField(primary_key=True,
                           max_length=11,
                           validators=[MinLengthValidator(11)],
                           blank=False,
                           null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    dob = models.DateField(blank=False, null=False)

    class Meta:
        db_table = 'employee'

    def __str__(self):
        return f"{self.cpf} - {self.name} - {self.dob}"

    def get_cpf(self):
        return self.cpf

    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob


class Salary(models.Model):
    """Creates Salary table"""
    id = models.AutoField(primary_key=True, blank=False, null=False)
    date_pmt = models.DateField(blank=False, null=False)
    cpf = models.ForeignKey('coreapp.Employee', on_delete=models.CASCADE)
    salary = MoneyField(max_digits=7, decimal_places=2, blank=False, null=False, default_currency='BRL')
    deduction = MoneyField(max_digits=7, decimal_places=2, blank=False, null=False, default_currency='BRL')

    class Meta:
        db_table = 'salary'

    def __str__(self):
        return f"{self.date_pmt} - {self.cpf} - {self.salary} - {self.deduction}"

    def get_id(self):
        return self.id

    def get_date_pmt(self):
        return self.date_pmt

    def get_cpf(self):
        return self.cpf

    def get_salary(self):
        return self.salary

    def get_deduction(self):
        return self.deduction
