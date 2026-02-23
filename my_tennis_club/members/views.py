from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world! <strong>Im John Carlo Baracena from IT241</strong>")
