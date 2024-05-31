from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bird, Toy
from .forms import FeedingForm
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def bird_index(request):
  birds = Bird.objects.all()
  return render(request, 'birds/index.html', { 'birds': birds })

def bird_detail(request, bird_id):
  bird = Bird.objects.get(id=bird_id)
  # Get the toys the bird doesn't have
  toys_bird_doesnt_have = Toy.objects.exclude(id__in = bird.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'birds/detail.html', {
    # Add the toys to be displayed
    'bird': bird, 'feeding_form': feeding_form, 'toys': toys_bird_doesnt_have
  })

class BirdCreate(CreateView):
  model = Bird
  fields = ['name', 'species', 'description', 'age']

class BirdUpdate(UpdateView):
  model = Bird
  fields = ['species', 'description', 'age']

class BirdDelete(DeleteView):
  model = Bird
  success_url = '/birds/'

def add_feeding(request, bird_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the bird_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.bird_id = bird_id
    new_feeding.save()
  return redirect('bird-detail', bird_id=bird_id)

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'

def assoc_toy(request, bird_id, toy_id):
  # Note that you can pass a toy's id instead of the whole object
  Bird.objects.get(id=bird_id).toys.add(toy_id)
  return redirect('bird-detail', bird_id=bird_id)