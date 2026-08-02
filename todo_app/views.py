from django.shortcuts import redirect, render
from todo_app.models import Todo

# Create your views here.
def home(request):
    todo = Todo.objects.all()
    return render(request, 'index.html', {"todo": todo})
from django.shortcuts import render, redirect
from .models import Todo

def addtask(request):
    if request.method == "POST":
        tasktitle = request.POST.get("tasktitle")
        taskdesc = request.POST.get("taskdesc")
        status = request.POST.get("status")

        print(tasktitle, taskdesc, status)

        if tasktitle and taskdesc and status:
            Todo.objects.create(
                tasktitle=tasktitle,
                taskdesc=taskdesc,
                status=status
            )
            return redirect("home")

    todo = Todo.objects.all()
    return render(request, "addtask.html", {"todo": todo})

def edit_todo(request,id):  
    todo = Todo.objects.get(id=id)
    return render(request,'edit.html',{"todo":todo})

def delete_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('home')

def update_todo(request, id):
    todo = Todo.objects.get(id=id)

    if request.method == "POST":
        todo.tasktitle = request.POST.get("tasktitle")
        todo.taskdesc = request.POST.get("taskdesc")
        todo.status = request.POST.get("status")

        todo.save()
        return redirect("home")