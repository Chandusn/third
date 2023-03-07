from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app3_first(request):
    return HttpResponse('App3 of First Function')

def app3_second(request):
    return HttpResponse('App3 of second Function')