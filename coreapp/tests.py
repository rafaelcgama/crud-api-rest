# from faker import Factory
from django.test import TestCase
from coreapp.models import Employee, Salary
from coreapp.serializers import EmployeeSerializer, SalarySerializer

# faker = Factory.create()

######### Test Models ##########
class EmployeeModelTestCase(TestCase):

    def test_types(self):
        """'Test model data types """
        # employee = EmployeeFactory()
        employee = Employee()

        date_type = Employee._meta.get_field('dob').get_internal_type()
        self.assertEqual(str(employee), employee.cpf)
        self.assertEqual(str(employee), employee.name)
        self.assertEqual(date_type, type(employee.dob))


class SalaryModelTestCase(TestCase):

    def test_types(self):
        """'Test model data types """
        salary = Salary()
        date_type = Salary._meta.get_field('date_pmt').get_internal_type()
        money_type = Salary._meta.get_field('salary').get_internal_type()
        self.assertEqual(date_type, type(salary.date_pmt))
        self.assertEqual(str(salary), salary.cpf)
        self.assertEqual(str(salary), salary.cpf)
        self.assertEqual(money_type, type(salary.salary))
        self.assertEqual(money_type, type(salary.deduction))