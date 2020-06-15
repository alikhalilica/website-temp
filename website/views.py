from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
    return render(request,"base.html")

def contact (request):
    return HttpResponse("contact")

def about(request):
    return HttpResponse("about")