from django.db import models

class History(models.Model):
    desc = models.TextField()

    def __str__(self):
        return self.desc
    
class Coll(models.Model):
    desc = models.TextField()
    
    def __str__(self):
        return self.desc

class Greed(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    year = models.BigIntegerField()
    image = models.ImageField(upload_to='history/', blank=True, null=True)

    def __str__(self):
        return self.name
