from django.shortcuts import render
from frontend import *

def moshin1(request):
    return render(request, "index.html")

def moshin2(request):
    return render(request, "index1.html")

def moshin3(request):
    return render(request, "index2.html")  

def moshin4(request):
    return render(request, "index3.html")

def moshin5(request):
    return render(request,"index4.html") 

def moshin6(request):
    return render(request, "index5.html")       
