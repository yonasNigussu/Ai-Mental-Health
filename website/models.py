from django.db import models
from django.utils.timezone import now

class Blog(models.Model):
    name = models.CharField(max_length=50)  # Store the name dynamically
    title = models.CharField(max_length=255)
    detail = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set created timestamp

    def __str__(self):
        return self.title
class Comment(models.Model):
    name = models.CharField(max_length=255, default='Anonymous')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Add timestamp

    def __str__(self):
        return f'{self.name} - {self.comment[:50]}...' #For admin panel readability
class Comment(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Add timestamp

    def __str__(self):
        return f'{self.name} - {self.comment[:50]}...' #For admin panel readability