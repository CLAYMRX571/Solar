from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=25)
    date = models.IntegerField()
    location = models.CharField(max_length=200)
    title = models.CharField()

    def __str__(self):
        return self.name
    
    def __str_(self):
        return self.date.strftime("%d-%m")