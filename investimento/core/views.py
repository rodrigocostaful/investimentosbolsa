from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    raise ValueError()
    return HttpResponse('Olá,mundo!')
