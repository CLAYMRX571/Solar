from django.db import models

class Journal(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Table(models.Model):
    name = models.CharField(max_length=255)
    price = models.BigIntegerField(default=0)

    def __str__(self):
        return self.name
    
class Detail(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    
    def __str__(self):
        return self.name
    
class Text(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.ImageField(upload_to='journal', blank=True, null=True)
    list = models.CharField(max_length=200)
   
    def __str__(self):
        return self.name
