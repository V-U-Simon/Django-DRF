from django.views import generic
from django.urls import reverse_lazy
from . import models


class TodoListView(generic.ListView):
    model = models.TaskModel
    template_name = "app_todo/todo_list.html"


class TodoDetailView(generic.DetailView):
    model = models.TaskModel
    template_name = "app_todo/todo_detail.html"


class TodoCreateView(generic.CreateView):
    model = models.TaskModel
    template_name = "app_todo/todo_form.html"
    fields = "__all__"


class TodoUpdateView(generic.UpdateView):
    model = models.TaskModel
    template_name = "app_todo/todo_form.html"
    fields = "__all__"


class TodoDeleteView(generic.DeleteView):
    model = models.TaskModel
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("app_todo:list")
