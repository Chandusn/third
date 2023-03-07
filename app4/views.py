from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app4_first(request):
    return HttpResponse('App4 of First Function')

def app4_second(request):
    return HttpResponse('App4 of second Function')