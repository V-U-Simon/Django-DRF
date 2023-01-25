from django.urls import path
from .views import TodoCreateView, TodoListView, TodoUpdateView, TodoDeleteView, TodoDetailView

app_name = 'app_todo'

urlpatterns = [
    path('', TodoListView.as_view(), name='list'),
    path('create/', TodoCreateView.as_view(), name='create'),
    path('<int:pk>/', TodoDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', TodoUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', TodoDeleteView.as_view(), name='delete'),
]