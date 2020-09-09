from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogs, BlogData
# Create your views here.

def home(response):
	bg = Blogs.objects.all()
	return render(response, "home/home.html", {"blog":bg})


def about(response):
	return render(response, "home/about.html", {})

def blog(response):
	return render(response, "home/blog.html", {})