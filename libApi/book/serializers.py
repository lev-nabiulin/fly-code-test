from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):

    author = SlugRelatedField(slug_field='name', queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'author')

class AuthorSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)

        instance.save()
        return instance