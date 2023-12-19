from django.forms import ModelForm, Textarea
from django import forms
from .models import Card

class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['activity', 'due_date', 'complete_date']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'complete_date': forms.DateInput(attrs={'type': 'date'}),
        }
    
