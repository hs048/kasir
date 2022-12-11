from django.db import models

# Create your models here.
class Berita(models.Model):
    title = models.CharField(max_length=255, unique=True)
    thumb = models.URLField(blank=True, null=True)
    author = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)
    time = models.CharField(max_length=50, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    key = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title