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

You can choose between en-us and pt-br. Just go to settings and change the LANGUAGE_CODE variable. In addition, if you want to run the docker-compose the following DATABASE changes must be done in the ['settings'](api_crud/settings.py) file:

* 'HOST': 'host.docker.internal'
* 'PORT': '3307'

In my machine (Windows) it is advisable to first run it locally and then deploy the docker if you also want to test the application without the docker. Once the docker is deployed, I couldn't get Django to connect to MYSQL locally again. It keeps trying to connect to the docker host even after I stopped and even deleted all containers, images and even the docker software itself. I am still trying to a workaround, but so far, I could only run it locally again after reinstalling MYSQL.

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

