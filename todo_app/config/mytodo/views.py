from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from .models import Task
from .forms import TaskForm

class indexView(View):
    def get(self, request):
        todo_list = Task.objects.all()
        context = {
            "todo_list": todo_list
        }
        return render(request, "mytodo/index.html", context)

class Addview(View):
    def get(self, request):
        form = TaskForm()
        return render(request, "mytodo/add.html", {'form': form})
        
    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'mytodo/add.html', {'form': form})

class Update_task_complete(View):
    def post(self, request):
        task_id = request.POST.get('task_id')
        task = Task.objects.get(id=task_id)
        task.complete = not task.complete
        task.save()
        return redirect('/')


class Updateview(View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        form = TaskForm(instance=task)
        return render(request, "mytodo/update.html", {'form': form, 'task_id': task_id})
        
    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'mytodo/update.html', {'form': form, 'task_id': task_id})

update = Updateview.as_view()


index = indexView.as_view()
add = Addview.as_view()
update_task_complete = Update_task_complete.as_view()
update = Updateview.as_view()

