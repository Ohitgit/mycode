# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.blog_list, name='blog_list'),  # Home page with list of blogs
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),  # View single blog
    path('upload/', views.blog_upload, name='blog_upload'),
    
    
]

