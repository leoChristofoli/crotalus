from django.db import models


class Message(models.Model):
    email = models.EmailField(
        blank=True
    )
    first_name = models.CharField(
        max_length=255,
        blank=True
    )
    last_name = models.CharField(
        max_length=255,
        blank=True
    )
    subject = models.CharField(
        max_length=255,
        blank=True
    )
    text = models.TextField(
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
