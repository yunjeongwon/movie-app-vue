from rest_framework import serializers

from ..models import Movie, Genre, Tag, Comment


class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tag
    fields = '__all__'

