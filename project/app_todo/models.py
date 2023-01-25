from django.db import models
from django.urls import reverse
# фукнция получения модели юзера из имени определенноого в settings.py
from django.contrib.auth import get_user_model
User = get_user_model()

class TaskModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='done')

class DoneTaskModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='in_progress')

class TaskModel(models.Model):
    title = models.CharField(max_length=255)
    task = models.TextField()
    deadline = models.DateField()
    STATUS_CHOICES = (
        ('done', 'Done'),
        ('in_progress', 'In Progress'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    project = models.ForeignKey('ProjectModel', on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True)

    objects = models.Manager()
    active = TaskModelManager()
    done = DoneTaskModelManager()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("app_todo:detail", kwargs={"pk": self.pk})
    

    def save(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        if user:
            self.user = user
        super().save(*args, **kwargs)

    
    
    
class ProjectModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
