from django.shortcuts import render,redirect
from app1.models import employee
from app1.form import employeeForm
def new_emp(request):
    data=employee.objects.all()
    form=employeeForm()
    if request.method=='POST':
        form=employeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home_page')
    context={'data':data,'form':form}
    return render(request,'app1_tem/home.html',context)
