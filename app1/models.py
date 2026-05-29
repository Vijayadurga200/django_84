from django.db import models


class employee(models.Model):
    empid=models.IntegerField(unique=True)
    emp_name=models.CharField(max_length=20)
    emp_salary=models.FloatField()
    
