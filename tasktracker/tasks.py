from __future__ import absolute_import, unicode_literals
from celery import shared_task
from tasktracker.models import Task, TaskTracker
from datetime import timedelta, datetime
from dateutil import tz

from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)

local_tz = tz.gettz('Asia/Kolkata')


@shared_task
def dailyUpdate():
	tasks = {}
	requiredTime = datetime.now(tz = local_tz).date() #Tasks created at or after this time will be sent through mail

	for i in range(1, 5):
			tasks[i] = Task.objects.filter(task_type = i, created_at__gte = requiredTime) #filtering the task based on task type and task creation datetime

	tasktrackers = TaskTracker.objects.filter(update_type = "Daily")

	logger.debug("------ Daily Updates ------\n")
	for tracker in tasktrackers:
		emailId = tracker.email #email id of the task tracker to which the updates are to be send
		taskType = tracker.task_type #type of tasks to send for updates

		for obj in tasks[taskType]:
			msg = str(datetime.now()) + '\t' + emailId + '\t' + str(taskType) + '\t' + obj.task_desc + '\n'
			logger.debug(msg) #logging in the file

	return None

@shared_task
def weeklyUpdate():
	tasks = {}
	requiredTime = datetime.now(tz = local_tz).date() - timedelta(days=7)

	for i in range(1, 5):
			tasks[i] = Task.objects.filter(task_type = i, created_at__gte = requiredTime)

	tasktrackers = TaskTracker.objects.filter(update_type = "Weekly")

	logger.debug("------ Weekly Updates ------\n")
	for tracker in tasktrackers:
		emailId = tracker.email
		taskType = tracker.task_type

		for obj in tasks[taskType]:
			msg = str(datetime.now()) + '\t' + emailId + '\t' + str(taskType) + '\t' + obj.task_desc + '\n'
			logger.debug(msg)

	return None

@shared_task
def monthlyUpdate():
	tasks = {}
	requiredTime = (datetime.now(tz = local_tz).date() - timedelta(days = 1)).replace(day = 1)

	for i in range(1, 5):
			tasks[i] = Task.objects.filter(task_type = i, created_at__gte = requiredTime)

	tasktrackers = TaskTracker.objects.filter(update_type = "Monthly")

	logger.debug("------ Monthly Updates ------\n")
	for tracker in tasktrackers:
		emailId = tracker.email
		taskType = tracker.task_type

		for obj in tasks[taskType]:
			msg = str(datetime.now()) + '\t' + emailId + '\t' + str(taskType) + '\t' + obj.task_desc + '\n'
			logger.debug(msg)

	return None
