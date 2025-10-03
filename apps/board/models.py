from django.db import models

class Board(models.Model):
    desc = models.TextField()

    def __str__(self):
        return self.desc
    
class Ses(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Member(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='hamkasb', blank=True, null=True)
    telegram = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Bar(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Car(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='ishchilar', blank=True, null=True)
    telegram = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)

    def __str__(self):
        return self.name