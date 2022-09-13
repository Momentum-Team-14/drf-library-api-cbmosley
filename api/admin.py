from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Book, BookTracker, BookNotes
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["email", "username",]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book)
admin.site.register(BookTracker)
admin.site.register(BookNotes)
