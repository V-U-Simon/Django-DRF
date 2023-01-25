from django.contrib import admin
from .models import TaskModel, ProjectModel

@admin.register(TaskModel)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'deadline', 'created_at', 'updated_at')
    list_filter = ('status', 'deadline', 'user')
    search_fields = ('title', 'task',)

@admin.register(ProjectModel)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
