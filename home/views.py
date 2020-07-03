from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def index(request):
    return HttpResponse('Hello!\nThis is a site contains all apis of CHNG.\nIngore if you have no idea.')