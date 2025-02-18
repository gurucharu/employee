from rest_framework import serializers
from .models import Employee, Salary

class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    salaries = SalarySerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'
    
