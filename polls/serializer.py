from rest_framework import serializers
from . import models

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Business
        fields = ('id','title','description','address',[])

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ('id','first_name','last_name')

class EmployedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employed
        fields = ('id','employed_by','employ_who','start_date','end_date')
