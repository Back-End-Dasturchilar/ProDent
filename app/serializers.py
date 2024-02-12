from rest_framework import serializers
from .models import Article, Home, Next, About, Authors, Tag, ServiceNext, Service, Blog


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class NextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Next
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class ServiceNextSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceNext
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
