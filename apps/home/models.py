from django.db import models

class Banner(models.Model):
    name = models.CharField(max_length=255)
  
    def __str__(self):
        return self.name
    
class Home(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='itm', blank=True, null=True)
    desc = models.TextField()
    button_name = models.CharField(max_length=100)
    buttons_name = models.CharField(max_length=100)
    buttons_image = models.ImageField(upload_to='home', blank=True, null=True)
    buttons_desc = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Messages(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=50)
    desc = models.TextField()
    image = models.ImageField(upload_to='message', blank=True, null=True)
    button = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Latest(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='latest', blank=True, null=True)
    button = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Slide(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='members', blank=True, null=True)

    def __str_(self):
        return self.name
    
class Slides(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='part', blank=True, null=True)

    def __str_(self):
        return self.name