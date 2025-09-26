from django.db import models

class Support(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='project', blank=True, null=True)

    def __str__(self):
        return self.name