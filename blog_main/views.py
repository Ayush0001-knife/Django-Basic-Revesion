from django.http import HttpResponse
from django.shortcuts import render

from blogs.models import Category

def home(request):
      return render(request,"home.html") 

def category(request):
      categories = Category.objects.all()
      context={
            'categories':categories
      }
      return render(request,"category.html",context)