from django.shortcuts import render, redirect

from .models import Todo

def home(request):
    if request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get("description")
        status = request.POST.get("status")

        if title and desc:  
            Todo.objects.create(
                title = title,
                desc = desc,
                status = status
            )
        return redirect("/")
    data = {
        'todos':Todo.objects.all().order_by('-id')
    }
    return render(request,'todo.html',context=data)

def delete_todo(request,id):
    try:
        todo = Todo.objects.get(id=id)
    except:
        return render(request,'delete.html',{'message':"Bunday topshiriq topilmadi"})
    
    if request.method == "POST":
        todo.delete()
        return redirect("/")
    
    
    return render(request,'delete.html',{'todo':todo})

def edit_todo(request, id):
    try:
        todo = Todo.objects.get(id=id)
    except:
        return render(request, 'edit.html', {'message': "Bunday topshiriq topilmadi"})
    
    if request.method == "POST":
        todo.title = request.POST.get("title")
        todo.desc = request.POST.get("description")
        todo.status = request.POST.get("status")
        todo.save()
        return redirect("/")
    
    return render(request, 'edit.html', {'todo': todo})

def detail_todo(request, id):
    try:
        todo = Todo.objects.get(id=id)
    except:
        return render(request, 'detail.html', {'message': "Bunday topshiriq topilmadi"})
    
    return render(request, 'detail.html', {'todo': todo})