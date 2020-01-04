from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import TodoListForm
from .models import TodoList, Category

# Create your views here.

def home(request): #the index view

    todos = TodoList.objects.all() #quering all todos with the object manager
    categories = Category.objects.all() #getting all categories with object manager

    if request.method == 'POST':
        form = TodoListForm(request.POST, request.FILES)
        if form.is_valid():  # False value is the problem
            form.save()
            return redirect('home')
        else:
            return HttpResponse("Your form is missing some required fields, Please go back and fill out the missing fields")
    form = TodoListForm()

    return render(request, "todoApp/home.html", {"todos": todos, "categories":categories, 'form': form})

def complete(request, pk):
    post = get_object_or_404(TodoList, pk=pk)
    if request.method =='GET':
        post.delete()
        return redirect('home')
    return render(request, "todoApp/home.html", {'object':post})


def edit(request, pk):
    task_selected= get_object_or_404(TodoList, pk=pk)
    form = TodoListForm(request.POST or None, instance=task_selected)

    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, "todoApp/edit.html", {'form':form})
