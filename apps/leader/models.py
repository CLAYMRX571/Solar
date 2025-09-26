from django.db import models

class Leader(models.Model):
    name = models.CharField(max_length=250)
    more_name = models.CharField(max_length=50)
    desc = models.TextField()
    image = models.ImageField(upload_to='data', blank=True, null=True)
    title = models.CharField(max_length=50)
    title_desc = models.TextField()
    file = models.FileField(upload_to='pdf', blank=True, null=True)
    file_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name