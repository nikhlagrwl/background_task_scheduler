from django.urls import path, include
from tasktracker.views import createTask, createTaskTracker


urlpatterns = [
    path('createTask/', createTask),
    path('createTaskTracker/', createTaskTracker),
]
