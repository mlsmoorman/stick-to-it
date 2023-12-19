from django.forms import ModelForm, Textarea
from django import forms
from .models import Card

class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['activity', 'due_date', 'complete']
        # widgets = {
		# 	'due_date': Textarea(attrs={'type':'date'})
		# }
        # due_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'})
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }
    
