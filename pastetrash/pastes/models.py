from django.db import models

from django.contrib.auth.hashers import make_password, check_password
from django.utils.text import slugify
# Create your models here.
class Paste(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True, editable=False)
    syntax = models.CharField(max_length=100)
    password = models.CharField(max_length=100, null=True, blank=True)
    owner = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
    
    def check_password(self, password):
        return check_password(password, self.password)

    def save(self, *args, **kwargs):
        # Empty values
        if not self.title:
            raise ValueError("Title is empty")

        if not self.content:
            raise ValueError("Content is empty")

        # Slug
        self.slug = slugify(self.title)
        # Password
        if self.password:
            self.password = make_password(self.password)
        super(Paste, self).save(*args, **kwargs)