from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Contact, ContactNext
from .serializers import ContactSerializer, ContactNextSerializer


class ContactAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactNextAPIView(generics.ListAPIView):
    queryset = ContactNext.objects.all()
    serializer_class = ContactNextSerializer
