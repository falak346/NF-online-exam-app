from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Administrator HOME PAGE")
def register(request):
    return HttpResponse("do the changes appear?")