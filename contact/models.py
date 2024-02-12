from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=212)
    email = models.EmailField()
    subject = models.CharField(max_length=212)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContactNext(models.Model):
    title = models.CharField(max_length=212)
    authors_image = models.ImageField(upload_to='Author')
    description = models.TextField()
    address = models.TextField()
    opening_hours = models.TextField()
    phone = models.CharField(max_length=212)
    days = models.CharField(max_length=212)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
