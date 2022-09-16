from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('books/', views.BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),
    path('tracker-list/', views.TrackerList.as_view(), name='tracker-list'),
    path('tracker-list/<int:pk>/',
         views.TrackerDetail.as_view(), name='tracker-detail'),
    path('books/<int:book_pk>/notes',
         views.BookNoteList.as_view(), name='notes-list'),
    path('notes/<int:pk>/', views.BookNoteDetail.as_view(), name='notes-detail'),
    path('', views.api_root),

]
