from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Day 1 challenge completed!")

def about(request):
    return HttpResponse("Day 1 About url created!")