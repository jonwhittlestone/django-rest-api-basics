from rest_framework import serializers

from postings.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            'pk',
            'user',
            'title',
            'content',
            'timestamp'
        ]
        read_only_fields = ['user']

    def validate_title(self, value):
        """We want the title to be unique"""

        qs = BlogPost.objects.filter(title__iexact=value) # including instance
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise serializers.ValidationError("This title has already been used")
        return value
