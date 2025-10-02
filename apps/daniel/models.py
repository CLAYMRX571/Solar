from django.db import models

class Daniel(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    image = models.ImageField(upload_to='daniel', blank=True, null=True)
    title = models.TextField()

    def __str__(self):
        return self.name
    
class Recep(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.ImageField(upload_to='command/', blank=True, null=True)

    def __str__(self):
        return self.name