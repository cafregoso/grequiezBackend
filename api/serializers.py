from django.db.models.expressions import fields
from rest_framework import serializers
from blog.models import Blog
from newsletter.models import Newsletter

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            'title',
            'content1',
            'content2',
            'content3',
            'resume',
            'created',
            'principla_image',
            'image1',
            'image2',
        ]

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = [
            'name', 
            'email', 
            'created',
        ]