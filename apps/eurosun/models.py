from django.db import models

class Eurosun(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Conf(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    mail = models.CharField(max_length=200)
    button = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Sun(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.ImageField(upload_to='sun/', blank=True, null=True)

    def __str__(self):
        return self.name