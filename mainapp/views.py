from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import datetime

from .forms import SignUpForm
from .models import Task


def main_page(request):
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todolist')
        else:
            print(form.errors)  # Print out form errors for debugging
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})

@login_required
def todolist(request):
    notStartedTasks = Task.objects.filter(status='Not Started')
    inProgressTasks = Task.objects.filter(status='In Progress')
    return render(request, 'main/todolist.html', {'notStarted':notStartedTasks, 'inProgress': inProgressTasks})

@login_required
def completed(request):
    completedTasks = Task.objects.filter(status='Completed')
    return render(request, 'main/completed.html', {'completed':completedTasks})

@csrf_exempt
@login_required
def todolist_process(request):
    if request.method == 'POST':
        
        details = request.POST.get('details')
        
        # Create a new patient entry in the database using the Patient model
        task = Task(user=request.user, status='Not Started', details=details)
        task.save()
        notStartedTasks = Task.objects.filter(status='Not Started')
        inProgressTasks = Task.objects.filter(status='In Progress')
        render(request, 'main/todolist.html', {'notStarted':notStartedTasks, 'inProgress': inProgressTasks})
        return redirect('todolist')
    else:
        return HttpResponse("Invalid Method")
    
@csrf_exempt
@login_required
def change_status(request,id):
    if request.method == 'POST':
        details = Task.objects.get(pk= id).details
        task = Task(id= id,user= request.user, status='In Progress',details= details, data_added = datetime.datetime.now())
        task.save()
        notStartedTasks = Task.objects.filter(status='Not Started')
        inProgressTasks = Task.objects.filter(status='In Progress')
        render(request, 'main/todolist.html', {'notStarted':notStartedTasks, 'inProgress': inProgressTasks})
        return redirect('todolist')
    else:
        return HttpResponse("Invalid Method")
    
@csrf_exempt
@login_required
def do_completed(request,id):
    if request.method == 'POST':
        details = Task.objects.get(pk= id).details
        task = Task(id= id,user= request.user, status='Completed',details= details, data_added = datetime.datetime.now())
        task.save()
        completedTasks = Task.objects.filter(status='Completed')
        render(request, 'main/completed.html', {'tasks':completedTasks})
        return redirect('todolist')
    else:
        return HttpResponse("Invalid Method")
    
@csrf_exempt
@login_required
def delete(request, id):
    if request.method == 'POST':
        if Task.objects.get(id = id).status == 'Completed':    
            Task.objects.filter(id = id).delete()
            completedTasks = Task.objects.filter(status='Completed')
            render(request, 'main/completed.html', {'completed':completedTasks})
            return redirect('completed')
        else :
            Task.objects.filter(id = id).delete()
            notStartedTasks = Task.objects.filter(status='Not Started')
            inProgressTasks = Task.objects.filter(status='In Progress')
            render(request, 'main/todolist.html', {'notStarted':notStartedTasks, 'inProgress': inProgressTasks})
            return redirect('todolist')
    else:
        return HttpResponse("Invalid Method")