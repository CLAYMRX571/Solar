from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.name
