from django.db import models


# Create your models here.

class Article(models.Model):
    address = models.TextField()
    opening_hours = models.TextField()
    phone = models.CharField(max_length=212)
    days = models.CharField(max_length=212)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone


class Home(models.Model):
    image = models.ImageField(upload_to='Author')
    name = models.CharField(max_length=212)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Next(models.Model):
    image = models.ImageField(upload_to='Author')
    name = models.CharField(max_length=212)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class About(models.Model):
    image = models.ImageField(upload_to='Author')
    name = models.CharField(max_length=212)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Authors(models.Model):
    title = models.CharField(max_length=212)
    authors_image = models.ImageField(upload_to='Author')
    authors_name = models.CharField(max_length=212)
    profession = models.CharField(max_length=212)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=212)
    name = models.CharField(max_length=212)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ServiceNext(models.Model):
    name = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='Author')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=212)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    image = models.ImageField(upload_to='Author')
    title = models.CharField(max_length=212)
    description = models.TextField()
