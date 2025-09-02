from django.db import models

# Create your models here.

class bookapp(models.Model):
    Title = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    Isbn = models.CharField(unique=True)
    Published_date = models.DateField(max_length=255)
    Genre = models.CharField(max_length=255)
    Date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title
