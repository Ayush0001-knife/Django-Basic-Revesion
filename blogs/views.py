from django.shortcuts import render
from .models import Blogs, Category


def category_blogs(request, category_id):

    category = Category.objects.get(id=category_id)

    blogs = Blogs.objects.filter(category=category)

    context = {
        "category": category,
        "blogs": blogs
    }

    return render(request, "category_blogs.html", context)


def blog_detail(request, category_id, blog_slug):
    
    category = Category.objects.get(id=category_id)

    blog = Blogs.objects.get(category=category, slug=blog_slug)

    context = {
        "blog": blog
    }

    return render(request, "individual_blog.html", context)
