from django.shortcuts import render
from rest_framework import generics, filters
from .models import Post
from .serializers import PostSerializer
from django.db.models import Q

"""
Inherits from DRF generics to create views for the Post model handling CRUD functionality.
"""


class PostListCreateView(generics.ListCreateAPIView):
    """
    Handles listing a collection and creation of a single instance. Includes a search filter on the title, content, and category fields.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "content", "category"]

    def get_queryset(self):
        """
        If a search term is present, filters the queryset of the Post collection. Otherwise, returns all.
        """
        queryset = super().get_queryset()
        search_term = self.request.query_params.get("term", None)
        if search_term:
            queryset = queryset.filter(
                Q(title__icontains=search_term)
                | Q(content__icontains=search_term)
                | Q(category__icontains=search_term)
            )
        return queryset


class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieval, update, and deletion of a single Post instance.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
