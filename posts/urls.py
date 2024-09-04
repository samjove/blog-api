from django.urls import path
from .views import PostListCreateView, PostRetrieveUpdateDestroyView

"""
URL configuration within the posts app. Configures routes for CRUD functionality.
"""
urlpatterns = [
    path("", PostListCreateView.as_view(), name="post-list-create"),
    path("<int:pk>/", PostRetrieveUpdateDestroyView.as_view(), name="post-detail"),
]
