from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def login_view_auth(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/articles/create/")
    else:
        form = AuthenticationForm(request)
    context = {
        "form": form
    }
    return render(request, "accounts/login1.html", context)


# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is None:
            context = {"error": "Invalid username or password !!!!!!"}
            return render(request, "accounts/login.html", context)
        login(request, user)
        return redirect("/articles/create/")    
    return render(request, 'accounts/login.html', {})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/accounts/login/")
    return render(request, 'accounts/logout.html', {})


def register_view(request):
    form = UserCreationForm(request.POST or None)    
    if form.is_valid():
        user_obj = form.save()
        return redirect("/accounts/login/")
    context = {
        "form": form
    }
    return render(request, "accounts/register.html", context)


def check_username(request):
    username = request.POST.get('username')
    print(username)
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("<div style= 'color:red;' >This username already exists</div>")
    else:
        return HttpResponse("<div style= 'color:green;' >This username is available</div>")
