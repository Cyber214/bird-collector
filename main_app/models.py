from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# A tuple of 2-tuples
MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

# Add the Toy model
class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toy-detail', kwargs={'pk': self.id})

# Create your models here.
class Bird(models.Model):
  name = models.CharField(max_length=100)
  species = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  # move toy model above cat model
  toys = models.ManyToManyField(Toy)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse("bird-detail", kwargs={"bird_id": self.id})
  
  def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
  
# Add new Feeding model below bird model
class Feeding(models.Model):
  date = models.DateField('Feeding date')
  meal = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=MEALS,
    # set the default value for meal to be 'B'
    default=MEALS[0][0]
  )

  # Create a bird_id column in the database
  bird = models.ForeignKey(Bird, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_meal_display()} on {self.date}"
  
  # change the default sort
  class Meta:
    ordering = ['-date']