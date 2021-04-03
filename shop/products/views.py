from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'home.html',{"email":"jac@123","name":"jackson"})

def about(request):
    return HttpResponse("<h1>About page</h1>")

def contact(request):
    return HttpResponse("<h1>contact page</h2>")

def product(request):
    return HttpResponse("<h1>list of products..</h2>")