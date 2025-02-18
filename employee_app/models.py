from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    

    def __str__(self):
        return self.name

class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="salaries")
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.CharField(max_length=20) 


    def __str__(self):
        return f"{self.employee.name} - {self.salary}"
