from rest_framework import serializers

from django.contrib.auth import get_user_model

from ..models import Movie, Genre, Tag, Comment


User = get_user_model()


# 생성
class CommentSerializer(serializers.ModelSerializer):
  class UserSerializer(serializers.ModelSerializer):
    class Meta:
      model = User
      fields = ('username',)
  class MovieSerializer(serializers.ModelSerializer):
    class Meta:
      model = Movie
      fields = ('pk',)

  user = UserSerializer(read_only=True)
  movie = MovieSerializer(read_only=True)
  class Meta:
    model = Comment
    fields = '__all__'
