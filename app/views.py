from rest_framework import generics, viewsets
from .models import Article, Home, Next, About, Authors, Tag, ServiceNext, Service, Blog

from .serializers import ArticleSerializer, HomeSerializer, NextSerializer, AboutSerializer, AuthorsSerializer, \
    TagSerializer, ServiceNextSerializer, ServiceSerializer, BlogSerializer


class ArticleAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class TagAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class HomeAPIView(generics.ListAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer


class ServiceAPIView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceNextAPIView(generics.ListAPIView):
    queryset = ServiceNext.objects.all()
    serializer_class = ServiceNextSerializer

    # def get_queryset(self):
    #     tag = self.request.query_params.get('tag')
    #     category = self.request.query_params.get('cat')
    #     q = self.request.query_params.get('q')
    #     if q:
    #         return Home.objects.filter(title__icontains=q)
    #     if tag:
    #         return Home.objects.filter(tags__name__icontains=tag)
    #     if category:
    #         return Home.objects.filter(category__name__icontains=category)
    #     else:
    #         return Home.objects.all()


class AboutAPIView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class AuthorsAPIView(generics.ListAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer


class NextAPIView(generics.ListAPIView):
    queryset = Next.objects.all()
    serializer_class = NextSerializer


class BlogAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
