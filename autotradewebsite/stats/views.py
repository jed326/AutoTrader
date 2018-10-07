from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def stats(request):
    return render(request, 'stats.html')