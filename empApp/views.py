from django.shortcuts import render
from empApp.models import Employee
from email import message
from multiprocessing import context
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from empApp.models import Employee
from empApp.forms import EmployeeForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def list(request):
    emp = Employee.objects.all()
    context = {'employees' : emp}
    
    return render(request, 'list.html', context)

def create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data saved successfully')
            return redirect('list')
    
    else:
        form= EmployeeForm()

    context= {'title': 'Create Employee', 'form':form}
    return render(request, 'create.html',context)