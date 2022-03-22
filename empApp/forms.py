from django import forms
from empApp.models import Employee

DESIGNATION_CHOICES = [
        ('Developer', 'Developer'),
        ('Network Engineer', 'Network Engineer'),
        ('Server Admin', 'Server Admin'),
        ('Manager', 'Manager'),
    ]

class EmployeeForm(forms.ModelForm):
  designation = forms.ChoiceField(widget=forms.RadioSelect,choices=DESIGNATION_CHOICES)
  class Meta:
    model= Employee
    fields= "__all__"