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

    orders = models.ManyToManyField(
        "users.User", through="movies.MovieOrder", related_name="ordered_movies"
    )


class MovieOrder(models.Model):
    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE, related_name="movies_orders")

    order_user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="user_movies_orders")

    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
        
        
        
        
    

   
