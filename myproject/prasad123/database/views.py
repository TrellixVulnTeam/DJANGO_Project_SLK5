from django.shortcuts import render
from database.models import Employee

# Create your views here.

def counter(request):
    data_prac = Employee.objects.all()
    print(data_prac)
    '''for x in data_prac:
        print(x)'''
    return render(request,"index.html",{'data' : data_prac})
