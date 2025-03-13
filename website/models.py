from django.db import models

# Create your models here.


class Blog(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=255)
    detail = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
