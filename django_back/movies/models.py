from django.db import models

from django.conf import settings

User = settings.AUTH_USER_MODEL


class Genre(models.Model):
  name = models.CharField(max_length=50)


class Tag(models.Model):
  name = models.CharField(max_length=50)

class Movie(models.Model):
  ids = models.IntegerField()
  evaluate_users = models.ManyToManyField(User, related_name="evaluate_movies")
  wish_users = models.ManyToManyField(User, related_name="wish_movies")
  genre_ids = models.ManyToManyField(Genre, related_name="genre_movies") #
  tag_ids = models.ManyToManyField(Tag, related_name="tag_movies") #
  backdrop_path = models.CharField(max_length=200) #
  original_language = models.CharField(max_length=10) #
  original_title = models.CharField(max_length=100) # 
  overview = models.TextField() # 
  popularity = models.FloatField() #
  poster_path = models.CharField(max_length=200) #
  release_date = models.CharField(max_length=20)#
  title = models.CharField(max_length=100) #
  vote_average = models.FloatField() #
  vote_count = models.IntegerField() #
  running_time = models.IntegerField() #
  trailer_path = models.TextField() #



class Comment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="comments")
  content = models.TextField()
  score = models.FloatField()



class Evaluate(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  score = models.IntegerField()
