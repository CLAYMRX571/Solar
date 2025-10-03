from django.db import models

class Support(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Miss(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()

    def __str__(self):
        return self.name

class Invol(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.name