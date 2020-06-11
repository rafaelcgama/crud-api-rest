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

##### User Credentials:
* **username:** rafael
* **email:** rafaelcgama@gmail.com
* **username:** 123capital

##### API URLS
Use HTML form
* **Admin:** http://localhost:8000/admin/coreapp/
* **User Registration:** http://127.0.0.1:8000/api/v1/rest-auth/registration/
* **User Login:** http://127.0.0.1:8000/api/v1/rest-auth/login/
* **User Logout:** http://127.0.0.1:8000/api/v1/rest-auth/login/


Use raw data
* **Employee Create and List:** http://127.0.0.1:8000/api/v1/employee/
* **Employee Retrieve, Update and Delete:** http://127.0.0.1:8000/api/v1/employee/{numero_do_CPF_registrado}/
* **Salary Create and List:** http://127.0.0.1:8000/api/v1/employee/
* **Salary Retrieve, Update and Delete:** http://127.0.0.1:8000/api/v1/salary/{numero_do_id}/
* **Extra calculations:** http://localhost:8000/api/v1/calculations/

