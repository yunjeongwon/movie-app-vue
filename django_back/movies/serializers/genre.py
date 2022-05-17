from rest_framework import serializers

from ..models import Movie, Genre, Tag, Comment


class GenreSerializer(serializers.ModelSerializer):
  class Meta:
    model = Genre
    fields = '__all__'

