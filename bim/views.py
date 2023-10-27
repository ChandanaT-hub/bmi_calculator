from django.http import HttpResponse
from django.shortcuts import render

def start(request):
    return render(request,'simple.html')

def calculate(request):
    w=float(request.GET.get('WEIGHT',''))
    h=float(request.GET.get('HEIGHT',''))
    bmi=float(w/(h**2))
    params={'var':bmi}
    return render(request,'simple2.html',params)
