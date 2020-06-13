from faker import Factory, Faker
from django.test import TestCase, Client
from django.urls import reverse, resolve
from coreapp.models import Employee, Salary
from django.contrib.auth.models import User
from factory import DjangoModelFactory, SubFactory
from rest_framework.authtoken.models import Token
from coreapp.serializers import EmployeeSerializer, SalarySerializer, MoneyFieldClass
from coreapp.views import EmployeeViewSet, SalaryViewSet, CalculationsView
from rest_framework import status
from datetime import date, datetime
from django.urls import path, include
from rest_framework.test import APITestCase, URLPatternsTestCase, APIClient, force_authenticate

fake = Faker()
fake.seed_instance(0)

# Creates Salary Factory
class EmployeeFactory(DjangoModelFactory):
    class Meta:
        model = Employee
        django_get_or_create = ('cpf', 'name', 'dob')

    cpf = str(fake.pyint(min_value=10000000000, max_value=99999999999))
    name = fake.name()
    dob = fake.date_of_birth()

############### EMPLOYEES #######################
####### Model Tests #########
class EmployeeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.employee = EmployeeFactory()

    def test_employee_creation(self):
        self.assertIsInstance(self.employee, Employee)

    def test_dtypes(self):
        self.assertIsInstance(self.employee.cpf, str)
        self.assertIsInstance(self.employee.name, str)
        self.assertTrue(isinstance(self.employee.dob, date))

    def test_all_fields_populated(self):
        self.assertTrue(self.employee.cpf)
        self.assertTrue(self.employee.name)
        self.assertTrue(self.employee.dob)

    def test_cpf_numbers(self):
        self.assertEqual(len(self.employee.cpf), 11)


####### View Tests ##########
class EmployeeViewTest(TestCase):
    urlpatterns = [
        path('api/v1/', include('coreapp.urls'))
    ]

    def setUp(self):
        self.client = APIClient()
        self.username = 'unit_test'
        self.user = User.objects.create_user(username='unit_test',
                                             email='unit_test@example.com',
                                             password='123finalmente')
        Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.auth_token.key)
        self.new_employee = {
            'cpf': '99999999999',
            'name': 'New Guy',
            'dob': '12/12/2000'
        }
        self.response = self.client.post(reverse('employee-list'),
                                         self.new_employee,
                                         format='json',
                                         REMOTE_USER=self.username
                                         )

    def test_authorization_is_enforced(self):
        """Test that the api has user authorization."""
        url = reverse('employee-list')
        new_client = APIClient()
        res = new_client.get(url, kwargs={'cpf': self.new_employee['cpf']}, format="json")
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    # Test List and Create
    def test_create_list(self):
        url_list_create = reverse('employee-list')

        # Test Create
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 1)
        self.assertEqual(Employee.objects.get().cpf, self.new_employee['cpf'])

        # Test List
        response_list = self.client.get(url_list_create,
                                        self.new_employee,
                                        format='json',
                                        REMOTE_USER=self.username
                                        )
        self.assertEqual(response_list.status_code, status.HTTP_200_OK)
        self.assertEqual(Employee.objects.count(), 1)
        self.assertEqual(Employee.objects.get().cpf, self.new_employee['cpf'])

    # Test Retrieve
    def test_retrieve(self):
        employee_retrieve = Employee.objects.get(cpf=self.new_employee['cpf'])
        resp_retrieve = self.client.get(
            reverse('employee-detail', kwargs={'pk': employee_retrieve.cpf}),
            format='json'
        )
        self.assertEqual(resp_retrieve.status_code, status.HTTP_200_OK)

    # Test Update giving all attributes and the change to be executed
    def test_update_all_attrs(self):
        employee_update = Employee.objects.get()
        change_employee = {
            'cpf': '99999999999',
            'name': 'Something new',
            'dob': '12/12/2000'
        }
        resp_update = self.client.put(
            reverse('employee-detail', kwargs={'pk': employee_update.cpf}),
            change_employee,
            format='json'
        )
        self.assertEqual(resp_update.status_code, status.HTTP_200_OK)

    # Test Update giving only the attribute to be changed
    def test_update_one_attrib(self):
        employee_update = Employee.objects.get()
        change_employee = {'name': 'Something new'}
        resp_update = self.client.patch(
            reverse('employee-detail', kwargs={'pk': employee_update.cpf}),
            change_employee,
            format='json'
        )
        # force_authenticate(resp_update, user=self.username, token=self.user.auth_token)
        self.assertEqual(resp_update.status_code, status.HTTP_200_OK)

    # Test Delete
    def test_delete(self):
        employee_delete = Employee.objects.get()
        resp_delete = self.client.delete(
            reverse('employee-detail', kwargs={'pk': employee_delete.cpf}),
            format='json',
            follow=True)
        self.assertEquals(resp_delete.status_code, status.HTTP_204_NO_CONTENT)


class EmployeeSerializerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.employee = EmployeeFactory()

    def setUp(self):
        self.serializer = EmployeeSerializer(self.employee)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['cpf', 'name', 'dob']))

    def test_columns_content(self):
        data = self.serializer.data
        self.assertEqual(data['cpf'], self.employee.cpf)
        self.assertEqual(data['name'], self.employee.name)
        self.assertEqual(data['dob'], self.employee.dob.strftime("%d/%m/%Y"))















############ SALARY TESTS #############
# Creates Salary factory
class SalaryFactory(DjangoModelFactory):
    class Meta:
        model = Salary
        django_get_or_create = ('date_pmt', 'cpf', 'salary', 'deduction')

    date_pmt = fake.date_this_decade()
    cpf = SubFactory(EmployeeFactory)
    salary = fake.pydecimal(right_digits=2, max_value=100000)
    deduction = fake.pydecimal(right_digits=2, max_value=100000)



####### Model Tests #########
class SalaryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.cpf = EmployeeFactory()
        cls.salary = SalaryFactory(cpf=cls.cpf)

    def test_employee_creation(self):
        self.assertIsInstance(self.salary, Salary)

    def test_dtypes(self):
        self.assertIsInstance(self.salary.date_pmt, date)
        self.assertIsInstance(self.salary.cpf, str)
        self.assertIsInstance(self.salary.salary, float)
        self.assertIsInstance(self.salary.deduction, float)

    def test_all_fields_populated(self):
        self.assertTrue(self.salary.date_pmt)
        self.assertTrue(self.salary.cpf)
        self.assertTrue(self.salary.salary)
        self.assertTrue(self.salary.deduction)

    def test_cpf_numbers(self):
        self.assertEqual(len(self.salary.id), 11)


####### View Tests ##########
class SalaryViewTest(TestCase):
    urlpatterns = [
        path('api/v1/', include('coreapp.urls'))
    ]

    def setUpTestData(cls):
        cls.cpf = EmployeeFactory()
        cls.salary = SalaryFactory(cpf=cls.cpf)

    def setUp(self):
        self.client = APIClient()
        self.username = 'unit_test'
        self.user = User.objects.create_user(username='unit_test',
                                             email='unit_test@example.com',
                                             password='123finalmente')
        Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.auth_token.key)
        self.new_salary = {
            'date_pmt': fake.date_this_decade(),
            'cpf': self.salary.cpf,
            'salary': fake.pydecimal(right_digits=2, max_value=100000),
            'deduction': fake.pydecimal(right_digits=2, max_value=100000)
        }
        self.response = self.client.post(reverse('salary-list'),
                                         self.new_salary,
                                         format='json',
                                         REMOTE_USER=self.username
                                         )

    def test_authorization_is_enforced(self):
        """Test that the api has user authorization."""
        url = reverse('salary-list')
        new_client = APIClient()
        res = new_client.get(url, kwargs={'id': self.new_salary['id']}, format="json")
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    # Test List and Create
    def test_create_list(self):
        url_list_create = reverse('salary-list')

        # Test Create
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Salary.objects.count(), 1)
        self.assertEqual(Salary.objects.get().id, self.new_salary['id'])

        # Test List
        response_list = self.client.get(url_list_create,
                                        self.new_salary,
                                        format='json',
                                        REMOTE_USER=self.username
                                        )
        self.assertEqual(response_list.status_code, status.HTTP_200_OK)
        self.assertEqual(Salary.objects.count(), 1)
        self.assertEqual(Salary.objects.get().id, self.new_salary['id'])

    # Test Retrieve
    def test_retrieve(self):
        salary_retrieve = Salary.objects.get(cpf=self.new_salary['id'])
        resp_retrieve = self.client.get(
            reverse('salary-detail', kwargs={'pk': salary_retrieve.id}),
            format='json'
        )
        self.assertEqual(resp_retrieve.status_code, status.HTTP_200_OK)

    # Test Update giving all attributes
    def test_update_all_attrs(self):
        salary_update = Salary.objects.get()
        change_salary = {
            'date_pmt': fake.date_this_decade(),
            'cpf'
            'salary': fake.pydecimal(right_digits=2, max_value=100000),
            'deduction': fake.pydecimal(right_digits=2, max_value=100000)
        }
        resp_update = self.client.post(
            reverse('salary-detail', kwargs={'pk': salary_update.id}),
            change_salary,
            format='json'
        )
        self.assertEqual(resp_update.status_code, status.HTTP_200_OK)

    # Test Update giving only the attribute to be changed
    def test_update_one_attrib(self):
        salary_update = Salary.objects.get()
        change_employee = {'name': 'Something new'}
        resp_update = self.client.patch(
            reverse('salary-detail', kwargs={'pk': salary_update.id}),
            change_employee,
            format='json'
        )
        # force_authenticate(resp_update, user=self.username, token=self.user.auth_token)
        self.assertEqual(resp_update.status_code, status.HTTP_200_OK)

    # Test Delete
    def test_delete(self):
        salary_delete = Salary.objects.get()
        resp_delete = self.client.delete(
            reverse('salary-detail', kwargs={'pk': salary_delete.id}),
            format='json',
            follow=True)
        self.assertEquals(resp_delete.status_code, status.HTTP_204_NO_CONTENT)


class SerializerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.cpf = EmployeeFactory()
        cls.salary = SalaryFactory(cpf=cls.cpf)

    def setUp(self):
        self.serializer = SalarySerializer(self.salary)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['date_pmt', 'cpf', 'salary', 'deduction']))

    def test_columns_content(self):
        data = self.serializer.data
        self.assertEqual(data['date_pmt'], self.salary.date_pmt.strftime("%d/%m/%Y"))
        self.assertEqual(data['cpf'], self.salary.cpf)
        self.assertEqual(data['salary'], self.salary.salary)
        self.assertEqual(data['deduction'], self.salary.deduction)




