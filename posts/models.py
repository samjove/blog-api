from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=100)
    tags = ArrayField(models.CharField(max_length=100, blank=True))
    
    def __str__(self):
        return self.name