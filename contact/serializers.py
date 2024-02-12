from rest_framework import serializers
from .models import Contact, ContactNext


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class ContactNextSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactNext
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
