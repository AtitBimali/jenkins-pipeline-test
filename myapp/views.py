from django.shortcuts import render

# Create your views here.
#trigger jenkins

def home(request):
    return render(request,'home.html')