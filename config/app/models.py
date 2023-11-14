# app/models.py
from django.db import models


class Todo(models.Model):
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'
    PRIORITY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]

    title = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default=MEDIUM)

# Remove any other import statements related to 'Todo'
