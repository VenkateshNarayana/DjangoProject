from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mydjapp/index.html')

def contactform(request):
    return render(request, 'mydjapp/contactform.html')