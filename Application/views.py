from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home/home.html', {}) 
    
def index(request):
    return render(request, 'home/index.html', {}) 
   # return render(request, 'home/page.html', context) 

def profile(request):
    return render(request, 'home/profile.html', {}) 

def generic(request):
    return render(request, 'home/generic.html', {}) 

def elements(request):
    return render(request, 'home/elements.html', {}) 


#def link(request):
#    return HttpResponse('<p>link</p>')

# Create your views here.
