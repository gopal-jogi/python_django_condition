from django.shortcuts import render

# Create your views here.
def index(request):
    d={'a':20, 'b':30, 'c':10}
    return render(request,'index.html',d)
