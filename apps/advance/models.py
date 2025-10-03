from django.db import models

class Advance(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    topic = models.CharField(max_length=100)
    performance = models.CharField(max_length=100)
    image = models.ImageField(upload_to='advance', blank=True, null=True)
    
    def __str__(self):
        return self.name