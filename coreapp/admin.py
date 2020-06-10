from django.contrib import admin
from coreapp.models import Employee, Salary

# Register your models here.
admin.site.register([Employee, Salary])