from django.http import request
from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'user/home.html')

def dff(request):
    return render(request, 'user/registration.html')

def ureg(request):
    if request.method == "POST":
        return render(request, 'user/registration.html')
    else:
        return render(request, 'user/registration.html')
