from django.db import models

# Create your models here.
class Business(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    address = models.CharField(max_length=30)

class Employee(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=30)

class Employed(models.Model):
    employed_by = models.ForeignKey(Business,on_delete=models.CASCADE)
    employ_who = models.ForeignKey(Employee,on_delete=models.CASCADE)
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(null=True,blank=True)


