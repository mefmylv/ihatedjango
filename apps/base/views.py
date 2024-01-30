from django.shortcuts import render
from apps.base import models

# Create your views here.
def index(request):
    title = "Geeks"
    settings = models.Settings.objects.latest('id')
    projects = models.Projects.objects.all()
    service = models.Service.objects.all()
    portfolio = models.Portfolio.objects.latest('id')
    qualification = models.Qualification.objects.all()
    lastproject = models.LastProject.objects.all()
    review = models.Review.objects.all()
    plan = models.Plan.objects.all()
    lastblog = models.LastBlog.objects.all()

    return render(request, 'base/index.html', locals())
    

def contact(request):
    settings = models.Settings.objects.latest('id')
    return render(request, 'base/contact.html', locals())
