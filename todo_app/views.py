import datetime
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

# Class based views
class index(ListView):
    model = Task
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["today"] = datetime.date.today()
        return context

    def post(self, *args, **kwargs):
        name = self.request.POST.get('name')
        priority = self.request.POST.get('priority')
        date = self.request.POST.get('date')
        todo = Task(name=name,priority=priority,date=date)
        todo.save()
        messages.success(self.request, "Successfully created the Todo Item.")
        return redirect('/')

class show(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'todo'

class update(UpdateView):
    model = Task
    template_name = 'edit.html'
    fields = ("name", "priority", "date")
    context_object_name = 'todo'

    def get_success_url(self):
        messages.success(self.request, "Successfully updated the Todo Item.")
        return reverse_lazy('todo_app:details', kwargs={'pk': self.object.id })

class destroy(DeleteView):
    model = Task    
    success_url = reverse_lazy('todo_app:home')

    def post(self, request, *args, **kwargs):
        messages.success(self.request, "Successfully deleted the Todo Item.")
        return super().post(request, *args, **kwargs)


# Function based views


# def index(request):
#     todos = Task.objects.all()
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         priority = request.POST.get('priority')
#         date = request.POST.get('date')
#         todo = Task(name=name,priority=priority,date=date)
#         todo.save()
#         messages.success(request, "Successfully created the Todo Item.")
#         return redirect('/')
#     today = datetime.date.today()    
#     context = {
#         'todos': todos,
#         'today': today
#     }
#     return render(request, 'index.html', context)


# def mark_as_done(request, todo_id):
#     todo = Task.objects.get(id=todo_id)
#     todo.delete()
#     messages.success(request, "Successfully completed the Task.")
#     return redirect('/')

# def update(request, todo_id):
#     todo = Task.objects.get(id=todo_id)
#     form = TodoForm(None, instance=todo)
#     if request.method == 'POST':
#         form = TodoForm(request.POST, instance=todo)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Successfully updated the Todo Item.")
#             return redirect('/')
#     return render(request, 'edit.html', { 'form': form })        