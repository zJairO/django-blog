from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    date = models.DateField()
    thumbnail = models.ImageField(upload_to='thumbnails', blank=True)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
       ordering = ['-date']

class Image(models.Model):
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.image.name
