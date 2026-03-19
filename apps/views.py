from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to MyProject!")


def home3(request):
    print("Testing branch on Git Hub")
    print("Testing branch on Git Hub from main branch")
    print("Now Made changes in main branch and now merging to test branch")
    return HttpResponse("Welcome to MyProject!")
