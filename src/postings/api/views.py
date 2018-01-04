from rest_framework import generics
from postings.models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field = 'pk'     # (?P<pk>\d+)
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        """Could override"""
        return BlogPost.objects.all()
