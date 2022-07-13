from django.db import models
from django.urls import reverse

# Create your models here.
class Race(models.Model):
    race_name= models.CharField(max_length=100)
    year = models.IntegerField(1900>=2050)
    race_type = models.CharField(max_length=100)
    distance = models.FloatField()
    image = models.URLField()
    
    def __str__(self):
        return self.race_name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'race_id': self.id})