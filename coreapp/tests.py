from faker import Factory, Faker
from django.test import TestCase, Client
from django.urls import reverse, resolve
from coreapp.models import Employee, Salary
from django.contrib.auth.models import User
from factory import DjangoModelFactory
from rest_framework.authtoken.models import Token
from coreapp.serializers import EmployeeSerializer, SalarySerializer
from coreapp.views import EmployeeViewSet, SalaryViewSet, CalculationsView
from rest_framework import status
from datetime import date, datetime
from django.urls import path, include
from rest_framework.test import APITestCase, URLPatternsTestCase, APIClient, force_authenticate

faker = Faker()
faker.seed_instance(0)


# class RemoteAuthenticatedTest(APITestCase):
#     client_class = APIClient
#
#     def setUp(self):
#         self.username = 'unit_test'
#         self.user = User.objects.create_user(username='unit_test',
#                                              email='unit_test@example.com',
#                                              password='123finalmente')
#         Token.objects.create(user=self.user)
#         super(RemoteAuthenticatedTest, self).setUp()


class EmployeeFactory(DjangoModelFactory):
    class Meta:
        model = 'coreapp.Employee'
        django_get_or_create = ('cpf', 'name', 'dob')

    cpf = str(faker.pyint(min_value=10000000000, max_value=99999999999))
    name = faker.name()
    dob = faker.date_of_birth()


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

    # Test Update giving all attributes
    def test_update_all_attrs(self):
        employee_update = Employee.objects.get()
        change_employee = {'name': 'Something new'}
        resp_update = self.client.patch(
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


class SerializerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.employee = EmployeeFactory()

    def setUp(self):
        # employee = {
        #     'cpf': self.employee.cpf,
        #     'name': self.employee.name,
        #     'dob': self.employee.dob
        # }
        # self.employee = Employee.objects.create(**employee)
        self.serializer = EmployeeSerializer(self.employee)
        # self.serializer.is_valid()

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['cpf', 'name', 'dob']))

    def test_columns_content(self):
        data = self.serializer.data
        self.assertEqual(data['cpf'], self.employee.cpf)
        self.assertEqual(data['name'], self.employee.name)
        self.assertEqual(data['dob'], self.employee.dob.strftime("%d/%m/%Y"))

# class EmployeeModelTest(APITestCase):
#     client = APIClient()
#
#     @staticmethod
#     def create_employee(cpf='', name='', dob=''):
#         if not len(cpf) and len(name) and not len(dob):
#             Employee.objects.create()
#
#
#
# class EmployeeModelTest(APITestCase, URLPatternsTestCase):
#     urlpatterns = [
#         path('api/v1/', include('coreapp.urls'))
#     ]
#
#     def test_create_employee(self):
#         url = reverse('employee-list')
#         # data = {
#         #     'cpf': '05028365988',
#         #     'name': 'Rafael',
#         #      'dob': '06/07/1984'
#         # }
#         response = self.client.get(url, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Employee.objects.count(), 1)
#         self.assertEqual(Employee.objects.get().name, 'Rafael')


# # ######### Test Models ##########
# # class EmployeeModelTestCase(TestCase):
# #
# #     def test_types(self):
# #         """'Test model data types """
# #         # employee = EmployeeFactory()
# #         employee = Employee()
# #
# #         date_type = Employee._meta.get_field('dob').get_internal_type()
# #         self.assertEqual(str(employee), employee.cpf)
# #         self.assertEqual(str(employee), employee.name)
# #         self.assertEqual(date_type, type(employee.dob))
# #
# #
# # class SalaryModelTestCase(TestCase):
# #
# #     def test_types(self):
# #         """'Test model data types """
# #         salary = Salary()
# #         date_type = Salary._meta.get_field('date_pmt').get_internal_type()
# #         money_type = Salary._meta.get_field('salary').get_internal_type()
# #         self.assertEqual(date_type, type(salary.date_pmt))
# #         self.assertEqual(str(salary), salary.cpf)
# #         self.assertEqual(str(salary), salary.cpf)
# #         self.assertEqual(money_type, type(salary.salary))
# #         self.assertEqual(money_type, type(salary.deduction))
