# Background Task Sheduler

This is a Django application used to create background task scheduler using celery.

Create a virtual environment and install the dependencies using requiremnts.txt (pip3 install -r requirements.txt).   
  
Run the Celery beat service for background tasks (celery -A convin worker -B -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler).  
  
Run the django backed server(python3 manage.py runserver).  
