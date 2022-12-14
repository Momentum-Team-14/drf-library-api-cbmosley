from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .models import Book, BookTracker, BookNote, CustomUser
from .serializers import BookSerializer, TrackerSerializer, BookNoteSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# Create your api views here.


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title',
                     'author']


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class TrackerList(generics.ListCreateAPIView):
    queryset = BookTracker.objects.all()
    serializer_class = TrackerSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user.id).order_by('book')


class TrackerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookTracker.objects.all()
    serializer_class = TrackerSerializer
    # permission_classes = (
    # permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user.id).order_by('book')


class BookNoteList(generics.ListCreateAPIView):
    queryset = BookNote.objects.all()
    serializer_class = BookNoteSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user.id).order_by('book')

    def perform_create(self, serializer):
        book = get_object_or_404(Book, pk=self.kwargs['book_pk'])
        serializer.save(user=self.request.user, book=book)


class BookNoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookNote.objects.all()
    serializer_class = BookNoteSerializer
    # permission_classes = (IsOwnerOrReadOnly)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user.id).order_by('book')


@ api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'books': reverse('book-list', request=request, format=format),
        'tracker': reverse('tracker-list', request=request, format=format),
        'notes': reverse('notes-list', request=request, format=format)
    })
