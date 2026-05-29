from django.contrib import admin
from app1.models import employee

class employeeAdmin(admin.ModelAdmin):
    list_display=['empid','emp_name','emp_salary']
    ordering=['empid']
admin.site.register(employee,employeeAdmin)