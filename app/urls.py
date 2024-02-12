from django.urls import path

from .views import *

urlpatterns = [
    path('article/', ArticleAPIView.as_view(), name='article'),
    path('blog/<int:pk>/', BlogAPIView.as_view(), name='blog'),
    path('next/', NextAPIView.as_view(), name='next'),
    path('about/', AboutAPIView.as_view(), name='about'),
    path('authors/', AuthorsAPIView.as_view(), name='authors'),
    path('service/next', ServiceNextAPIView.as_view(), name='service-next'),
    path('service/', ServiceAPIView.as_view(), name='service'),
    path('home/', HomeAPIView.as_view(), name='home'),
    path('tag/', TagAPIView.as_view(), name='tag'),
]
