from django.contrib.auth.models import User
from rest_framework import generics
from .models import Book, BookTracker, BookNote, CustomUser
from .serializers import BookSerializer, TrackerSerializer, BookNoteSerializer
# Create your api views here.


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class TrackerList(generics.ListCreateAPIView):
    queryset = BookTracker.objects.all()
    serializer_class = TrackerSerializer


class TrackerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookTracker.objects.all()
    serializer_class = TrackerSerializer


class BookNoteList(generics.ListCreateAPIView):
    queryset = BookNote.objects.all()
    serializer_class = BookNoteSerializer


class BookNoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookNote.objects.all()
    serializer_class = BookNoteSerializer
