from django.shortcuts import render, redirect
from tasks.models import Task
from tasks.form import TaskForm, SearchForm


def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        form = SearchForm()
        search = request.GET.get('search')
        category = request.GET.get('category')
        ordering = request.GET.get('ordering')
        if search:
            tasks = tasks.filter(title__icontains=search)
        if category:
            tasks = tasks.filter(category__id=category)

        return render(request, 'tasks/task_list.html', context={'tasks': tasks, 'form': form})
    

def task_detail(request, task_id):
    if request.method == 'GET':
        task = Task.objects.get(id=task_id)
        return render(request, 'tasks/task_detail.html', context={'task': task})
    

def task_create(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'tasks/task_create.html', context={'form': form})
    elif request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task.objects.create(**form.cleaned_data)
            return redirect('/tasks/')
        else:
            return render(request, 'tasks/task_create.html', context={'form': form})