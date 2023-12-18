from django.db import models
from django.urls import reverse

# Create your models here.
class Card(models.Model):
    activity = models.CharField(max_length=100)
    due_date = models.DateField('Due Date')
    complete_date = models.DateField('Complete Date')
    
    def get_absolute_url(self):
        return reverse('index')
    