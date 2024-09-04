from django.db import models
from django.contrib.postgres.fields import ArrayField

"""
Creates a Post model. Uses the postgres specific ArrayField to create a list of tags for the tag field.
"""


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=100)
    tags = ArrayField(models.CharField(max_length=100, blank=True))
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
