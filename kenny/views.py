from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "nakakapotangina.html")

def hello(request):
    return render(request, "hello.html")

def login(request):
    return render(request, "login.html")