from rest_framework import serializers

from django.contrib.auth import get_user_model

from ..models import Movie, Genre, Tag, Comment


User = get_user_model()

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
      model = Genre
      fields = ('name',)
  
class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tag
    fields = ('name',)


class MovieSerializer(serializers.ModelSerializer):
  genre = GenreSerializer(many=True)
  tag = TagSerializer(many=True)

  class Meta:
    model = Movie
    fields = ('pk', 'poster_url', 'title', 'running_time', 'genre', 'tag',)


class MovieEvaluateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = ('pk', 'poster_url', 'title', 'release_year',)


class MovieDetailSerializer(serializers.ModelSerializer):
  class CommentSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
      class Meta:
        model = User
        fields = ('username',)
    
    user = UserSerializer(read_only=True)

    class Meta:
      model = Comment
      fields = ('pk', 'score', 'user',)
  
  genre = GenreSerializer(many=True)
  tag = TagSerializer(many=True)
  comments = CommentSerializer(many=True, read_only=True)

  class Meta:
    model = Movie
    fields = ('pk', 'poster_url', 'title', 'running_time', 'genre', 'tag', 'release_year', 'description', 'trailer_url', 'age_range', 'comments',)
