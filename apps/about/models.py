from django.db import models

class About(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.ImageField(upload_to='about', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Key(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    title = models.CharField(max_length=50)
    ches = models.CharField(max_length=100)

    def __str__(self):
        return self.name
