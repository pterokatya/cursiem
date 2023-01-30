from django.shortcuts import render

# Create your views here.
def index(request):
    print("ASDASDASD")

    return render(request, "special/index.html")
def login(request):
    print("ASDASDASD")

    return render(request, "special/login.html")

# asd