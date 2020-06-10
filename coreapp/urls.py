# from django.urls import path, include
# from django.conf.urls import url, include
# from .views import *
# from django.urls import path, include
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from coreapp.views import SalaryViewSet, EmployeeViewSet

router = DefaultRouter()
router.register('employee', EmployeeViewSet, basename='employee')
router.register('salary', SalaryViewSet, basename='salary')

# urlpatterns = [
#     path('employees/', EmployeeList.as_view()),
#     path('salaries/', SalaryList.as_view())
# ]

urlpatterns = [
    url('^', include(router.urls)),
]