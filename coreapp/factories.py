from factory import DjangoModelFactory, SubFactory, Factory, random
from coreapp.models import Employee, Salary
from moneyed import Money
from faker import Faker
random.reseed_random(0)
# from faker.providers.currency import Provider

faker = Factory.create()

amount = faker.pydecimal(left_digits=7, right_digits=2, positive=True)
currency_code = faker.currency_code()


class EmployeeFactory(DjangoModelFactory):
    class Meta:
        model = Employee
        django_get_or_create = ('cpf', 'name', 'dob')

    cpf = Faker('cpf')
    name = Faker('employee')
    dob = Faker('date_object')


class SalaryFactory(DjangoModelFactory):
    class Meta:
        model = Salary
        django_get_or_create = ('date_pmt', 'cpf', 'salary', 'deduction')

    date_pmt = Faker('date_object')
    cpf = SubFactory(EmployeeFactory)
    salary = Salary.objects.create(salary=Money(amount, currency_code))
    deduction = Salary.objects.create(salary=Money(amount, currency_code))
