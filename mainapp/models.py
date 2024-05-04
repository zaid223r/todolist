from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    
    MY_CHOICES = (
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )
    
    user = models.ForeignKey(User, related_name='task', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=MY_CHOICES)
    details = models.TextField(max_length=1000)
    data_added = models.DateTimeField(auto_now_add=True)