from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'index.html', {'tasks': tasks, 'form': form})


def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'update.html', {'form': form})


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    return render(request, 'delete.html', {'item': item})


