from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def index(request):
    tasks = Task.objects.order_by('-created_at')

    if request.method == 'POST':
        # Add a task
        if 'add' in request.POST:
            title = request.POST.get('title', '').strip()
            if title:
                Task.objects.create(title=title)

        # Mark a task completed
        elif 'complete' in request.POST:
            task_id = request.POST.get('complete')
            task = get_object_or_404(Task, id=task_id)
            task.completed = True
            task.save()

        # Delete a task
        elif 'delete' in request.POST:
            task_id = request.POST.get('delete')
            task = get_object_or_404(Task, id=task_id)
            task.delete()

        return redirect('index')

    return render(request, 'todo/index.html', {'tasks': tasks})
