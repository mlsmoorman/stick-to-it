from django.shortcuts import render
from django.views.generic.edit import CreateView
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

class CardCreate(CreateView):
  model = Card
  fields = '__all__'

# Create your views here.
def cards_index(request):
  cards = Card.objects.all()
  return render(request, 'cards/index.html', { 'cards': cards })

def home(request):
  return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')

def cards_detail(request, card_id):
  card = Card.objects.get(id=card_id)
  return render(request, 'cards/detail.html', { 'card': card })