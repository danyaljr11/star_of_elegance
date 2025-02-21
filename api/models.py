from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='service_pictures/', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    before_pictures = models.JSONField(null=True, blank=True)  # Storing array of 'before' pictures as JSON
    after_pictures = models.JSONField(null=True, blank=True)   # Storing array of 'after' pictures as JSON

    def __str__(self):
        return self.name


class Rate(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    rate = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    state = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.rate})"


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    text = models.TextField()

    def __str__(self):
        return self.name


class Request(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('finished', 'Finished'),
    ]
    TYPE_CHOICES = [
        ('hotels', 'Hotels'),
        ('restaurants', 'Restaurants'),
        ('residential', 'Residential')
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    service_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')
    service_type = models.CharField(max_length=15, choices=TYPE_CHOICES, default=None)

    def __str__(self):
        return f"{self.name} ({self.status})"
