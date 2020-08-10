from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

from tasktracker.models import Task, TaskTracker
from tasktracker.serializers import TaskSerializer, TaskTrackerSerializer


# Create your views here.

#View for creating or updating Tasks
@csrf_exempt
def createTask(request):
	if request.method == "POST":
		data = JSONParser().parse(request)
		serializer = TaskSerializer(data = data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status = 201)
		else:
			error = {}
			error['response'] = 'Enter valid credentials'
		return JsonResponse(error, status = 400)

	if request.method == 'PUT':
		data = JSONParser().parse(request)
		
		task = Task.objects.get(id = data['id'])

		if task is not None:
			task.task_desc = data['task_desc']
			task.task_type = data['task_type']
			task.save()
			return JsonResponse(task, status = 201)
		return JsonResponse(data, status = 400)

#View for creating Task Tracker
@csrf_exempt
def createTaskTracker(request):
	if request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = TaskTrackerSerializer(data = data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status = 200)
		else:
			error = {}
			error['response'] = 'Enter valid credentials'
		return JsonResponse(error, status = 400)


