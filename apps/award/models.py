from django.db import models

class Award(models.Model):
    desc = models.TextField()

    def __str__(self):
        return self.desc 
    
class Link(models.Model):
    name = models.CharField(max_length=200)
    awards = models.CharField(max_length=200)
    achieve = models.CharField(max_length=200)
    lead = models.CharField(max_length=200)
    fell = models.CharField(max_length=200)
    chall = models.CharField(max_length=200)
    jour = models.CharField(max_length=200)
    image = models.ImageField(upload_to='link/', blank=True, null=True)

    def __str__(self):
        return self.name