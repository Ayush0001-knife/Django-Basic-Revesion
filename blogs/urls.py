from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('<int:category_id>/', views.category_blogs, name='category_blogs'),
    path('<int:category_id>/<slug:blog_slug>/', views.blog_detail, name='blog_detail'),
]