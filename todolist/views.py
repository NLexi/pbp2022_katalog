from cgi import test
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from .models import Task
from .forms import MyForm
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist_item = Task.objects.filter(user = request.user)
    username = request.user.username
    context = {
    'list_item': data_todolist_item,
    'username' : username
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            return response
        else:
            messages.info(request, 'Wrong Username or Password!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    return response

def add_task(request):
    form = MyForm()
    if request.method == 'POST':
        form = MyForm(request.POST)       
        if form.is_valid():
            test = form.save()
            test.user = request.user
            test.save()
            return redirect('todolist:show_todolist')
    context = {'form' : form}
    return render(request, 'create-task.html', context)

def finish_task(request, id):
    item = Task.objects.get(user = request.user, id=id)
    item.is_finished = not item.is_finished
    item.save()
    return redirect('todolist:show_todolist')

def delete_task(request, id):
    item = Task.objects.get(user = request.user, id=id)
    item.delete()
    return redirect('todolist:show_todolist')