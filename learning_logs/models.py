from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """Temat poznawany przez uzytkownika"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Zwraca reprezentację modelu w postaci ciagu tekstowego"""
        return self.text


class Entry(models.Model):
    """Konkretne informacje o postępie w nauce"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Zwraca reprezentację modelu w postaci ciągu tekstowego"""
        return f'{self.text[:50]}...'
