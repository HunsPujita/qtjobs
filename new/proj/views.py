from django.shortcuts import render



def login(request):
    return render(request, "login.html")

def Register(request):
    return render(request, "Register.html")
