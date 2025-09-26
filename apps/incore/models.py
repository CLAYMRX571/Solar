from django.db import models
    
class Incore(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='itm/', blank=True, null=True)
    desc = models.TextField()
    button_name = models.CharField(max_length=100)
    buttons_name = models.CharField(max_length=100)
    buttons_image = models.ImageField(upload_to='home', blank=True, null=True)
    buttons_desc = models.CharField(max_length=100)

    def __str__(self):
        return self.name