from django.shortcuts import render

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from healthcare.forms import NewUserForm,SignUpForm
# add to your views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

def index(request):
    return render(request, "pink/index.html")

@login_required
def sucess(request):
    context = {}
    context['user'] = request.user
    return render(request, 'pink/dashboard.html', context)


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
           
            return redirect('student_login')
    else:
        form = SignUpForm()
    return render(request, 'pink/signup.html', {'form': form})

@login_required
def user_logout(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse("student_login"))


def Student_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('sucess'))
        else:
            context['error'] = "Provide valid credentials !"
            return render(request, "pink/login.html", context)
    else:
        return render(request, "pink/login.html", context)
