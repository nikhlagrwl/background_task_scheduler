from rest_framework import serializers
from tasktracker.models import Task, TaskTracker



class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = '__all__'


class TaskTrackerSerializer(serializers.ModelSerializer):
	class Meta:
		model = TaskTracker
		fields = '__all__'

