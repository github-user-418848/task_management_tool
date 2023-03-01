from django import forms
from .models import Dashboard

class DashboardForm(forms.ModelForm):
    class Meta:
        model = Dashboard
        fields = ['show_completed_tasks', 'task_sort_order']
