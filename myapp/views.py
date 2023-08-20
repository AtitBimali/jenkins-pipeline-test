from django.shortcuts import render

# Create your views here.
#trigger jenkins 2

def home(request):
    return render(request,'home.html')