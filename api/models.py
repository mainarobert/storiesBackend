from django.db import models

# Create your models here.

class Story(models.Model):
    title = models.TextField(null=True, blank=True)
    author = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title[0:30]