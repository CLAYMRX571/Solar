from django.db import models

class Membership(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    column_name = models.CharField(max_length=50)
    column_desc = models.CharField(max_length=200)
    column_button = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Text(models.Model):
    desc = models.TextField()

    def __str__(self):
        return self.desc
    
class Image(models.Model):
    image = models.ImageField(upload_to='mem/', blank=True, null=True)

    def __str__(self):
        return self.image
    
class Board(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    button = models.CharField(max_length=50)

    def __str__(self):
        return self.name