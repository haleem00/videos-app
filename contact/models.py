from datetime import datetime
from django.db import models


class Testi(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photo/testi')
    opinion = models.TextField()
    def __str__(self) :
        return self.name






class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    messages= models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now)
    
    def __str__(self) :
        return self.name



