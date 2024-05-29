from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('birds/', views.bird_index, name='bird-index'),
  path('birds/<int:bird_id>/', views.bird_detail, name='bird-detail'),
]