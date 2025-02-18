from django.shortcuts import render

from rest_framework import viewsets

from .models import Employee, Salary
from .serializers import EmployeeSerializer, SalarySerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
from rest_framework.response import Response
from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def list(self, request, *args, **kwargs):
        if not Employee.objects.exists():  # Check if the table is empty
            return Response({"message": "Employee list is empty"}, status=200)
        return super().list(request, *args, **kwargs)

