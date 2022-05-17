from django.db import models

from django_back.django_back import settings




class Movie(models.Model):
  like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movies")
  genre = 
  tag = 

  title = models.CharField(max_length=100)
  running_time = models.IntegerField()
  description = models.TextField()
  age_range = models.IntegerField()
  release_year = models.IntegerField()
  trailer_url = models.TextField()
  poster_url = models.TextField()

