from django.shortcuts import render

# Create your views here.
def land(request):
    return render(request,"landing.html")

def dashboard(request):
    return render(request,"landpage.html")

def archiv(request):
    return render(request,"archieved.html")