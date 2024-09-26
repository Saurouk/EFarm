from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogListView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
