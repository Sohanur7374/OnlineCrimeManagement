from django.shortcuts import render
from django.http import request
# Create your views here.


def mlog(request):
    return render(request, 'm_log/log.html')
def mreg(request):
    return render(request, 'm_log/reg.html')
