from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello from the index view in JobHunter app")
