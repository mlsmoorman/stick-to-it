from django.contrib import admin
from django.db import models
from django.urls import reverse
from django import forms

from django.contrib.auth.models import User

# Create your models here.
class Card(models.Model):
    activity = models.CharField(max_length=100)
    due_date = models.DateField(blank=True, null=True)
    complete_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('index')
    
