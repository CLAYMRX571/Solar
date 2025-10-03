from django.db import models

class Part(models.Model):
    desc = models.TextField()

    def __str__(self):
        return self.desc

class Cards(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.ImageField(upload_to='part', blank=True, null=True)
    link = models.CharField(max_length=255)
    button = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Pord(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=200)
    desc = models.TextField()

    def __str__(self):
        return self.name