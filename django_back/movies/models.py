from django.db import models

from django.conf import settings

User = settings.AUTH_USER_MODEL


class Genre(models.Model):
  name = models.CharField(max_length=50)


class Tag(models.Model):
  name = models.CharField(max_length=50)


class Movie(models.Model):
  wish_users = models.ManyToManyField(User, related_name="wish_movies")
  genre = models.ManyToManyField(Genre, related_name="genre_movies")
  tag = models.ManyToManyField(Tag, related_name="tag_movies")

  title = models.CharField(max_length=100)
  running_time = models.IntegerField()
  description = models.TextField()
  age_range = models.IntegerField()
  release_year = models.IntegerField()
  trailer_url = models.TextField()
  poster_url = models.TextField()


class Comment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="comments")
  content = models.TextField()
  score = models.FloatField()
