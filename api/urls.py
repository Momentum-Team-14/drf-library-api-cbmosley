from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>/', views.BookDetail.as_view()),
    path('books/tracker_list', views.TrackerList.as_view()),
    path('books/<int:pk>/tracker', views.TrackerDetail.as_view()),
    path('books/notes', views.BookNoteList.as_view()),
    path('notes/<int:pk>/', views.BookNoteDetail.as_view())

]
