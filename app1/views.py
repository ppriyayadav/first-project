from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def priya(request):
    return HttpResponse('priya is a bad girl')
def dhoni(request):
    return HttpResponse('dhoni is a best player')