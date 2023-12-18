from django.shortcuts import render

# some dummy/pre-database data
cards = [
  {'activity': 'Reading List', 
   'due_date': '2023-12-24',
   'complete_date': '',
   },
  {'activity': 'Car Maintenance', 
   'due_date': '2023-12-24',
   'complete_date': '',
   },
  {'activity': 'Shopping List', 
   'due_date': '2023-12-24',
   'complete_date': '2023-12-15',
  }
]

# Create your views here.

def home(request):
  return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')


def cards_index(request):
  return render(request, 'cards/index.html', {
    'cards': cards
  })