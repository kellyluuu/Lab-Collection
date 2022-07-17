from datetime import date
from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


# -------------------- Completed model M:M with Race model ------------------- #
class Completed(models.Model):
    completed_race = models.CharField(max_length=50)
        
    def __str__(self):
        return self.completed_race
        
    def get_absolute_url(self):
        return reverse('completed_detail', kwargs={'pk': self.id})
    

# -------------------- Race Model M:M with Completed model ------------------- #
class Race(models.Model):
    race_name= models.CharField(max_length=100)
    year = models.IntegerField(1900>=2050)
    race_type = models.CharField(max_length=100)
    distance = models.FloatField()
    image = models.URLField()
    completed = models.ManyToManyField(Completed)
    
    def __str__(self):
        return f"{self.year} {self.race_name}"
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'race_id': self.id})
    
    def training_for_race(self):
        return self.training_set.filter(activity = 'R' or 'B' or 'S' or 'W' or 'C' or 'O').count() > 0 
    
    class Meta:
        ordering = ['-year']


    
ACTIVITY = (
    ('R', 'Run'),
    ('B', 'Bike'),
    ('S', 'Swim'),
    ('W', 'Weight'),
    ('C', 'Cross-Fit'),
    ('O', 'Other')
)

# ------------------------- Training model w/ race fk ------------------------ #
class Training(models.Model):
    date = models.DateField('Training date')
    activity = models.CharField('Activity',
        max_length=1,
        choices= ACTIVITY,
        default = ACTIVITY[0][0]
        )
    distance = models.FloatField('distance - miles')
    
    duration = models.IntegerField('duration - minutes',
        default=60,
        validators=[MaxValueValidator(360), MinValueValidator(1)]
    )

    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_activity_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
   