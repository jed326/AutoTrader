from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def choosestock(request):
    return render(request, 'choosestock.html')