### Objective

The goal of this project is to create a REST API using the Python/Django Rest Framework and implement CRUD operations and a few extra calculations.

### Database
The database selected was MYSQL and it contains the following tables:

**Employee:**
* CPF number
* employee name
* day of birth

**Salary**
* date of payment
* CPF number
* salary paid
* deduction paid

**Extra Calculations** 

* Max Salary
* Min Salary
* Average Salary
* Average Deductions 


### Execution

You can choose between en-us and pt-br. Just go to settings and change the LANGUAGE_CODE variable 

##### Credentials:
If the project is run locally you have the option to create a superuser by running:

python manage.py createsuperuser

But in case the docker-compose is used, a regular user must be added by using the urls below.

##### API URLS
Use HTML form
* **Admin:** http://localhost:8000/admin/coreapp/
* **User Registration:** http://localhost:8000/api/v1/rest-auth/registration/
* **User Login:** http://localhost:8000/api/v1/rest-auth/login/
* **User Logout:** http://localhost:8000/api/v1/rest-auth/logout/


Use raw data
* **Employee Create and List:** http://localhost:8000/api/v1/employee/
* **Employee Retrieve, Update and Delete:** http://localhost:8000/api/v1/employee/{numero_do_CPF_registrado}/
* **Salary Create and List:** http:/localhost:8000/api/v1/employee/
* **Salary Retrieve, Update and Delete:** http://localhost:8000/api/v1/salary/{numero_do_id}/
* **Extra calculations:** http://localhost:8000/api/v1/calculations/

