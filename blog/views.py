from django.shortcuts import render, redirect

from account.forms import UserRegistrationForm
from blog.models import Blog
from .forms import BlogForm
from django.shortcuts import render
#from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_GET
import requests
 # Correct import
from .forms import BlogForm
from .utils import get_country_from_ip, get_client_ip
from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Blog

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('profile')
    return render(request, 'login.html')

@login_required
def profile(request):
    blogs = Blog.objects.filter(author=request.user)
    return render(request, 'profile.html', {'blogs': blogs})

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('profile')
    else:
        form = BlogForm()
    return render(request, 'create_blog.html', {'form': form})

from ipware import get_client_ip

def blog_list(request):
    if request.user.is_authenticated:
          client_ip,is_routable = get_client_ip(request)
          print('client_ip',client_ip)
          response = requests.get(f"http://ip-api.com/json/{client_ip}")
       
          if response.status_code == 200:
                    location_data = response.json()
                    print('location======',location_data)
                    country=location_data['country']
                    # country="India"
                    blogs=None
                    if  Blog.objects.filter(country=country,author=request.user).exists():
                        blogs=Blog.objects.filter(country=country,author=request.user)
                    else:
                                Blog.objects.create(country=country,author=request.user)
                    
                    country_title=Blog.objects.filter(country=country,author=request.user).first()           
                    return render(request, 'blog_list.html', {'blogs': blogs,'country_title':country_title})
          return render(request, 'blog_list.html')           
        
             
        #    return render(request, 'blog_list.html', {'blogs': blogs,'country_title':country_title})
    else:
        return redirect('login')


def blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})

def blog_upload(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user  # Set the current user as the author
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog_upload.html', {'form': form})
