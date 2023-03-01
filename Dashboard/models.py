from django.db import models
from Users.models import User

SORT_CHOICES = [
    ('date_created', 'Date Created'),
    ('due_date', 'Due Date'),
    ('priority', 'Priority'),
]

class Dashboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    show_completed_tasks = models.BooleanField(default=False)
    task_sort_order = models.CharField(choices=SORT_CHOICES, max_length=50)
    
    def __str__(self):
        return f"{self.user}'s Dashboard"