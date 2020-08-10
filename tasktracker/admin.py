from django.contrib import admin
from tasktracker.models import Task, TaskTracker

# Register your models here.


#Model registration and display for Task
class TaskAdmin(admin.ModelAdmin):
	list_display = ['id', 'task_type', 'task_desc', 'created_at']

admin.site.register(Task, TaskAdmin)

#Model registration and display for Task Tracker
class TastTrackerAdmin(admin.ModelAdmin):
	list_display = ['id', 'task_type', 'update_type', 'email']

admin.site.register(TaskTracker, TastTrackerAdmin)
