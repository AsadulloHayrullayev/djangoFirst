from django.shortcuts import render # type: ignore

def hello_view(request):
    return render (request,'hello.html')