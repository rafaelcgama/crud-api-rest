from django.db import models


# Create your models here.
class User(models.Model):
    cpf = models.ForeignKey('core.Salary',
                            max_length=11,
                            primary_key=True,
                            blank=False,
                            null=False,
                            on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False, null=False)
    dob = models.DateField(blank=False, null=False)

    def get_cpf(self):
        return self.cpf

    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob


class Salary(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    date_pmt = models.DateField(blank=False, null=False)
    cpf = models.ForeignKey('core.User',
                            max_length=11,
                            blank=False,
                            null=False,
                            on_delete=models.CASCADE)
    salary = models.FloatField(blank=False, null=False)
    deduction = models.FloatField(blank=False, null=False)

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

