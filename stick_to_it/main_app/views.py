from django.shortcuts import render, redirect
from django import forms
from django.forms import widgets
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

import datetime

from .models import Card
from .forms import CardForm


# Sign Up User:
def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
        else:
            error_message = "Invalid sign up - please try again!"
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "registration/signup.html", context)


# Create a new Activity Card
class CardCreate(LoginRequiredMixin, CreateView):
    model = Card
    # Uses modified form class from forms.py to enable 
    form_class = CardForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# Delete an Activity Card
class CardDelete(LoginRequiredMixin, DeleteView):
    model = Card
    success_url = "/cards"


# Update an Activity Card
class CardUpdate(LoginRequiredMixin, UpdateView):
    model = Card
    form_class = CardForm
    # fields = ['activity', 'due_date', 'complete_date']

# View user's Cards
@login_required
def cards_index(request):
    cards = Card.objects.filter(user=request.user).filter(complete_date=None)
    return render(request, "cards/index.html", {"cards": cards})

# Home Page
def home(request):
    return render(request, "home.html")

# About Page
def about(request):
    return render(request, "about.html")

# Detail Page
@login_required
def cards_detail(request, card_id):
    card = Card.objects.get(id=card_id)
    return render(request, "cards/detail.html", {"card": card})

# Completed Task Card Page
@login_required
def cards_archive(request):
    # filters cards and removes those that do not have a completed date
    cards = Card.objects.filter(user=request.user).exclude(complete_date=None)
    return render(request, 'cards/archive.html', { 'cards': cards })

# Complete Card Page 
@login_required
def cards_complete(request, card_id):
    # filters to the selected card and updates the date to today's date 
    Card.objects.filter(id=card_id).update(complete_date=datetime.date.today())
    return redirect('index')