from django.shortcuts import render
from .models import Card

# some dummy/pre-database data
# cards = [
#   {'activity': 'Reading List', 
#    'due_date': '2023-12-24',
#    'complete_date': '',
#    },
#   {'activity': 'Car Maintenance', 
#    'due_date': '2023-12-24',
#    'complete_date': '',
#    },
#   {'activity': 'Shopping List', 
#    'due_date': '2023-12-24',
#    'complete_date': '2023-12-15',
#    }
# ]

# Create your views here.
def cards_index(request):
  cards = Card.objects.all()
  return render(request, 'cards/index.html', { 'cards': cards })

def home(request):
  return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')

