from django.shortcuts import render
from django.http import HttpResponse
from .models import UserDetails, Info
from django.db import connection
# Create your views here.

# Using AND queries 
def index_(request):
    data = UserDetails.objects.filter(name = 'Thanos') & UserDetails.objects.filter(mobile = 11111)
    return render(request,'index.html',{'data':data})

# Using union queries
def index_(request):
    data = UserDetails.objects.all().values_list('name').union(Info.objects.all().values_list('address'))
    return render(request,'index.html',{'data':data})

# Using RAW SQL queires
def index(request):
    data = UserDetails.objects.raw('SELECT * FROM app_userdetails')
    return render(request,'index.html',{'data':data})

def index(request):

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM app_userdetails")
    x = cursor.fetchall()

    return render(request, 'index.html', {'data': x})