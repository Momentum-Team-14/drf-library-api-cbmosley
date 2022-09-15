from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, BookTracker, BookNote, CustomUser


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', 'author', 'publication_date', 'genre', 'featured')


class TrackerSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    book = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = BookTracker
        fields = ('status', 'book', 'user')


class BookNoteSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    book = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = BookNote
        fields = ('book', 'user', 'notes', 'created_at', 'privacy')
