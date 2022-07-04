from django.db.models.expressions import fields
from rest_framework import serializers
from blog.models import Blog
from newsletter.models import Newsletter


class UsernameRelated(serializers.RelatedField):

    def to_representation(self, value):
        return value.username

class BlogSerializer(serializers.ModelSerializer):
    user = UsernameRelated(read_only=True)
    class Meta:
        model = Blog
        fields = [
            'id',
            'title',
            'content1',
            'content2',
            'content3',
            'resume',
            'created',
            'principal_image',
            'image1',
            'image2',
            'user',
        ]

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = [
            'name', 
            'email', 
            'created',
        ]