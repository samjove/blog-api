from django.contrib import admin
from django.urls import path, include

'''
URL configuration for the blog api. 
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls'))
]
