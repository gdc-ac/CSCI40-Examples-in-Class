from django.urls import path
from .views import index, TaskListView, TaskDetailView

urlpatterns = [
    path('', index, name='index'),
    path('list', TaskListView.as_view(), name='list'),
    path('<int:pk>/detail', TaskDetailView.as_view(), name='task-detail'),
]

app_name = 'tasks'