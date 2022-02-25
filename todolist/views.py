from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method=="POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/todolist/') 
    context = {'tasks': tasks, 'form':form}
    return render(request, 'todolist/list.html',context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    
    if request.method=="POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/todolist/')
    context = {'form':form}
    return render(request, 'todolist/update_task.html', context)

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    
    if request.method=="POST":

        task.delete()
        return redirect('/todolist/')
    context = {'task':task}
    return render(request, 'todolist/delete_task.html', context)