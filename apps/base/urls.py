from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('contact/', contact, name="contact"),
    path('blog/', blog, name="blog"),
    path('blog_details/', blog_details, name="blog-details"),
    path('home_two/', home2, name="home_two"),
    path('home_three/', home3, name="home_three"),

]