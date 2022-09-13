from turtle import title
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.constraints import UniqueConstraint
# Create your models here.

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username

#title, author, publication date, a genre,
class Book(models.Model): 
    title = models.CharField(max_length=100, blank=True, default='')
    author = models.CharField(max_length=100, blank=True, default='')
    publication_date = models.DateField(blank = True, null = True)
    genre = models.CharField(max_length=100, blank=True, default='')
    featured = models.BooleanField(default=False)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['title', 'author'], name='unique_constraints')
        ]

    def __str__(self):
        return f'{self.title} by {self.author}'




class BookTracker(models.Model):
    READING = 'rg'
    READ = 'rd'
    UNREAD = 'ur'
    STATUS_CHOICES = [
        (READING, 'reading'),
        (READ, 'read'),
        (UNREAD, 'unread')
    ]

    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default=UNREAD)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='tracking_books')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tracking_users')

    def __str__(self):
        return f'{self.status}'



class BookNotes(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_notes')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='note_users')
    notes = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add = True)
    privacy = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.notes}'