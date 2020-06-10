# from django.urls import path, include
# from django.conf.urls import url, include
# from .views import *
# from django.urls import path, include
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from coreapp.views import SalaryViewSet, EmployeeViewSet

router = DefaultRouter()
router.register(r'employee', EmployeeViewSet)
router.register(r'salary', SalaryViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]