from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    button = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Cd(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='jamoa/', blank=True, null=True)
    telegram = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)

    def __str__(self):
        return self.name