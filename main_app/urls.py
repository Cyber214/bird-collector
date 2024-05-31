from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('birds/', views.bird_index, name='bird-index'),
  path('birds/<int:bird_id>/', views.bird_detail, name='bird-detail'),
  path('birds/create/', views.BirdCreate.as_view(), name='bird-create'),
  path('birds/<int:pk>/update/', views.BirdUpdate.as_view(), name='bird-update'),
  path('birds/<int:pk>/delete/', views.BirdDelete.as_view(), name='bird-delete'),
  path('birds/<int:bird_id>/add-feeding/', views.add_feeding, name='add-feeding'),
  path('toys/create/', views.ToyCreate.as_view(), name='toy-create'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy-detail'),
  path('toys/', views.ToyList.as_view(), name='toy-index'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy-update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy-delete'),
]
