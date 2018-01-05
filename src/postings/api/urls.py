from .views import BlogPostRudView, BlogPostAPIView
from django.conf.urls import url

urlpatterns = [
    url(r'^$', BlogPostAPIView.as_view(), name='post-listcreate'),
    url(r'^(?P<pk>\d+)$', BlogPostRudView.as_view(), name='post-rud'),
]
