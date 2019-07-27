from django.shortcuts import render
from task.forms import taskForm
from task.models import task


def home(request):
    if request.POST.get('delete'):
        tasks = task.objects.all()
        form = taskForm()
        task.objects.filter(id__in=request.POST.getlist('inputs')).delete()
        context = {
            'tasks':tasks,
            'form':form
        }
    elif request.method == 'POST':
        tasks = task.objects.all()
        form = taskForm(request.POST)
        if form.is_valid():
            form.save()
        context = {
            'tasks': tasks,
            'form': form
        }
    else:
        tasks = task.objects.all()
        form = taskForm()
        context = {
            'tasks': tasks,
            'form':form,
        }
    return render(request,'home.html',context)