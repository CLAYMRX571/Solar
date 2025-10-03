from django.db import models

class Challenge(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return self.name

class Galler(models.Model):
    image = models.ImageField(upload_to='challenge/', blank=True, null=True)

    def __str__(self):
        return self.image
    
class Anno(models.Model):
    desc = models.TextField()

    def __str__(self):
        return self.desc
    
class Wins(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='command/', blank=True, null=True)

    def __str__(self):
        return self.name