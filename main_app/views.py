from django.shortcuts import render

from django.http import HttpResponse

class Bird:
  def __init__(self, name, species, description, age):
    self.name = name
    self.species = species
    self.description = description
    self.age = age

birds = [
  Bird('Tweety', 'canary', 'Yellow and cheerful', 2),
  Bird('Polly', 'parrot', 'Talks a lot', 5),
  Bird('Sky', 'blue jay', 'Bright blue and lively', 3),
  Bird('Robin', 'robin', 'Red-breasted and energetic', 4)
]

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello 🕊Bird Brains🦅</h1>')

def about(request):
  return render(request, 'about.html')

def bird_index(request):
  return render(request, 'birds/index.html', { 'birds': birds })