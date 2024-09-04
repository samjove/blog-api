from rest_framework import serializers
from .models import Post

"""
Inherites DRF serializers to create a serializer for the Post model and all its fields.
"""


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
