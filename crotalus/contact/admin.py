from django.contrib import admin
from .models import Message

@admin.register(Message)
class MyUserAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'email')
    search_fields = ['first_name', 'last_name', 'email']