import datetime

from django.shortcuts import render, redirect, get_object_or_404

from .forms import TaskForm
from .models import Task


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')

    return render(request, 'tasks/home.html', {
        'form': TaskForm,
        'current_tasks': Task.objects.filter(completed__isnull=True).order_by('created').reverse(),
        'completed_tasks': Task.objects.filter(completed__isnull=False).order_by('completed').reverse()
    })


def complete_task(request, task_id: int):
    task = get_object_or_404(Task, id=task_id)
    task.completed = datetime.datetime.now()
    task.save()

    return redirect('home')


def delete_task(request, task_id: int):
    task = get_object_or_404(Task, id=task_id)
    task.delete()

    return redirect('home')
