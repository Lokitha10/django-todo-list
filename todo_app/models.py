from django.db import models

# Create your models here.
class Todo(models.Model):
    tasktitle = models.CharField(max_length=100)
    taskdesc = models.TextField()
    status = models.CharField(max_length=20)