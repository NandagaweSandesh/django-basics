from django.http import HttpResponse
from django.shortcuts import render
from employees.models import Employees

def home(response):
    employees = Employees.objects.all()
    # print(employees) if we refresh home page, if will print results in command prompt
    context = {
        'employees':employees
    }
    return render (response, 'home.html', context)