from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from coreapp.views import SalaryViewSet, EmployeeViewSet, CalculationsView

router = DefaultRouter() # Creates router dor ViewSet urls
router.register(r'employee', EmployeeViewSet)
router.register(r'salary', SalaryViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^calculations/$', CalculationsView.as_view()),
]
