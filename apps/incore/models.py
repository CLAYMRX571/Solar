from django.db import models
    
class Incore(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Core(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='core', blank=True, null=True)
    desc = models.TextField()
    core_name = models.CharField(max_length=255)
    core_image = models.ImageField(upload_to='cores', blank=True, null=True)
    core_desc = models.TextField()

    def __str__(self):
        return self.name

class Tess(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='tess', blank=True, null=True)
    desc = models.TextField()
    link = models.CharField(max_length=150)
    img = models.ImageField(upload_to='youtube', blank=True, null=True)

    def __str__(self):
        return self.name