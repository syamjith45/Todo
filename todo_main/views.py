from django.http import HttpResponse
from todo.models import Task
from django.shortcuts import render
def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-update_at')
    context={
        'tasks':tasks
    }
    return render(request,'home.html',context)