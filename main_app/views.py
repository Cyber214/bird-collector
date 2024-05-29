from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def bird_index(request):
  birds = Bird.objects.all()
  return render(request, 'birds/index.html', { 'birds': birds })