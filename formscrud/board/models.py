from django.db import models
from django.utils import timezone

class Board(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.title