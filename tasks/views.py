from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Task


def index(request):
    return HttpResponse("Hello World")


# Use list-based for a more custom approach
# def task_list(request):
#     tasks = Task.objects.all()
#     ctx = {
#         "tasks": tasks
#     }

#     return render(request, 'task_list.html', ctx)

# def task_detail(request, pk):
#     task = Task.objects.get(pk=pk)
#     ctx = {
#         'task': task
#     }

#     return render(request, 'task_detail.html', ctx)


# Use class based if you want something simple
class TaskListView(ListView):
    model = Task
    template_name = "task_list.html"


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "task_detail.html"
