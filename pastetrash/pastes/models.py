from django.db import models

# Create your models here.
class Paste(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)
    syntax = models.CharField(max_length=100)
    password = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title