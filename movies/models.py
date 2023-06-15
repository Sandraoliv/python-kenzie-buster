from django.db import models


class RATING_CHOICES(models.TextChoices):
    G = ('G')
    PG = ('PG')
    PG_13 = ('PG-13') 
    R = ('R') 
    NC_17 = ('NC-17') 
      
    
class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, blank=True, null=True, default=None)
    rating = models.CharField(
        max_length=20, choices=RATING_CHOICES.choices, blank=True,
        null=True, default=RATING_CHOICES.G)
    synopsis = models.TextField(blank=True, null=True, default=None)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name='movies', null=True)
        
        
        
        
    

   
