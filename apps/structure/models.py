from django.db import models

class Structure(models.Model):
    desc = models.TextField()

    def __str__(self):
        return self.desc

class Column(models.Model):
    desc = models.TextField()
    button = models.CharField(max_length=50)
    
    def __str__(self):
        return self.desc
    
class Card(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    button = models.CharField(max_length=50)

    def __str__(self):
        return self.name