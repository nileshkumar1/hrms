from django.db import models
from .models import *

class Emp(models.Model):
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    position = models.CharField(max_length=50)
    experience = models.CharField(max_length=50,)
    education = models.CharField(max_length=100)
    contact_no = models.IntegerField()


class Attendance(models.Model):
    emp_id = models.IntegerField()
    In_time = models.TimeField()
    Out_time =models.TimeField()
    
    
class Leave(models.Model):
    emp_id = models.IntegerField()
    Leave_Date = models.DateField()
    Resion = models.CharField(max_length=50)
    Status = models.CharField(max_length=20)
    
    
class Department(models.Model):
    emp_id = models.IntegerField()
    Name= models.CharField(max_length=100)
    Type = models.CharField(max_length=100)
    Total_emp = models.IntegerField()
    
class Emergency_contact(models.Model):
    emp_id = models.IntegerField()
    Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    contact = models.IntegerField()
    

    