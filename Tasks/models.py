from django.db import models
from Users.models import User

STATUS_CHOICES = [
    ('TODO', 'To Do'),
    ('IN_PROGRESS', 'In Progress'),
    ('DONE', 'Done'),
]

PRIORITY_CHOICES = [
    ('LOW', 'Low'),
    ('MEDIUM', 'Medium'),
    ('HIGH', 'High'),
]

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=50)
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=50)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
