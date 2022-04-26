from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def checkout(request):
    return render(request, 'checkout.html')
    
def store(request):
    return render(request, 'store.html')
    
def product(request):
    return render(request, 'product.html')

def blank(request):
    return render(request, 'blank.html')
    