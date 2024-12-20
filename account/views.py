from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('blog_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    """
    Logs out the user and redirects to the home page.
    """
    logout(request)
    return redirect('/')  # Redirect to the home page



from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                # Authenticate the user
                user = form.get_user()
                login(request, user)
                return redirect('blog_list')  # Redirect to the blog list or home page
            else:
                messages.error(request, "Invalid username or password")
                return render(request, 'login.html', {'form': form})
        else:
            form = AuthenticationForm()
            return render(request, 'login.html', {'form': form})  
    else:
        return redirect('blog_list')

