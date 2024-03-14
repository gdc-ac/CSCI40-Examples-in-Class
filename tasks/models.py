from datetime import datetime

from django.db import models
from django.urls import reverse


class TaskGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateTimeField(null=True)
    taskgroup = models.ForeignKey(
        TaskGroup, on_delete=models.CASCADE, related_name="tasks", default=1
    )

    def __str__(self):
        return "{} due on {}".format(self.name, self.due_date)

    def get_absolute_url(self):
        return reverse("tasks:task-detail", args=[self.pk])
        # lets django find the appropriate urls

    @property  # this function is not supposed to be called like a function but like a field
    def is_due(self):
        return datetime.now() >= self.due_date

    class Meta:
        ordering = ["due_date"]  # in ascending due date, -due_date for descending
        unique_together = ["name", "due_date"]
        # i want these fields to be unique together so i cannot create another instance with the same combination
        # can even do things like 2D lists to separate ruling, putting everything in one list forces just one combination for all in the table
        # using 2D lists lets u keep multiple constraints without affecting one another
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
