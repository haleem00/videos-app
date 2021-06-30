from django.db import models
from datetime import datetime



class Cat(models.Model):
    name = models.CharField(max_length=100)
    
    
    def __str__(self) :
        return self.name



class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to = 'photo')
    video = models.FileField(upload_to='video')
    is_published = models.BooleanField(default=True)
    video_date = models.DateTimeField(default=datetime.now)
    cat= models.ForeignKey(Cat,related_name="cat",on_delete=models.CASCADE,default=1)

    def __str__(self) :
        return self.title


 