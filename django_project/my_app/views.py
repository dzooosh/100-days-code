from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def hello(request, first_name:str) -> str:
    return HttpResponse(f"Hello {first_name}")

