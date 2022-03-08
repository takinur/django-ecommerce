from django.shortcuts import render
from empApp.models import Employee

# Create your views here.
def index(request):
    return render(request, 'index.html')

def list(request):
    emp = Employee.objects.all()
    context = {'employees' : emp}
    
    return render(request, 'list.html', context)