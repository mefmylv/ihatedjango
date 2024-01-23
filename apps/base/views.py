from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    title = "Geeks"
    settings = Settings.objects.latest('id')
    return render(request, 'index.html', locals())

def contact(request):
    settings = Settings.objects.latest('id')
    return render(request, 'contact.html', locals())

def blog(request):
    settings = Settings.objects.latest('id')
    return render(request, 'blog.html', locals())

def blog_details(request):
    settings = Settings.objects.latest('id')
    return render(request, 'blog-details.html', locals())


def home3(request):
    settings = Settings.objects.latest('id')
    return render(request, 'home-three.html', locals())


def home2(request):
    settings = Settings.objects.latest('id')
    return render(request, 'home-two.html', locals())
