from django.http.response import HttpResponse, HttpResponseBase
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    return render(request,'about.html')   
def services(request):
    return render(request,'services.html')    
def contact(request):
    return render(request,'contact.html')   
def home(request):
    return render(request,'home.html')