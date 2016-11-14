from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'tracking/index.html')

def track(request):
    return HttpResponse("TRACK")

def new(request):
    return HttpResponse("NEW")
