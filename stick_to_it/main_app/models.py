from django.db import models
from django.urls import reverse

# Create your models here.
class Card(models.Model):
    activity = models.CharField(max_length=100)
    due_date = models.DateField(blank=True)
    complete_date = models.DateField(blank=True)
    
    def get_absolute_url(self):
        return reverse('index')
    