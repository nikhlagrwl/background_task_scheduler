from django.db import models

# Create your models here.



TASK_CHOICES = ((1,1),(2,2),(3,3),(4,4))
UPDATE_CHOICES = (('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'))

#Model for Task
class Task(models.Model):
	task_type = models.IntegerField(choices = TASK_CHOICES, db_column = 'Task Type')
	task_desc = models.CharField(max_length = 500, db_column = 'Task Description')
	created_at = models.DateTimeField(auto_now_add = True, editable = False)

# Model for Task Tracker
class TaskTracker(models.Model):
	task_type = models.IntegerField(choices = TASK_CHOICES, db_column = 'Task Type')
	update_type = models.CharField(max_length = 10, choices = UPDATE_CHOICES, db_column = 'Update Type')
	email = models.EmailField(unique = True, db_column = 'Email')
