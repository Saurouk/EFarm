from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import BlogPost
from .serializers import BlogPostSerializer

# Vue pour lister les articles de blog
class BlogListView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]  # Seuls les admins peuvent créer des articles
        return []  # GET est accessible à tous

@method_decorator(login_required(login_url='/admin/login/'), name='dispatch')
# Vue pour créer un nouvel article de blog
class CreateBlogPostView(generics.CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAdminUser]  # Restreint l'accès aux utilisateurs admin
