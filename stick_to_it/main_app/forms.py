from django.forms import ModelForm, Textarea
from django import forms
from .models import Card

class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['activity', 'due_date', 'complete_date']
        # widgets are used to make an Admin Model form
        widgets = {
            # the DateInput widget changes the django 'type' from text to date creating a Date Picker
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'complete_date': forms.DateInput(attrs={'type': 'date'}),
            # the TextArea widget changes the input from text to a TextArea allowing user to see all of their inputs instead of having to scroll
            'activity': forms.Textarea(attrs={'rows':5, 'cols':16})
        }
       
    
