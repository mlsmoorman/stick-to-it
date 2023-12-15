from django.db import models

# Create your models here.
class Card(models.Model):
    activity = models.CharField(max_length=100)
    due_date = models.DateField
    complete_date = models.DateField
    