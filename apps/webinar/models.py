from django.db import models
from django.core.validators import FileExtensionValidator

class Webinar(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return self.name
    
class Bros(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Bobs(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    
    def __str__(self):
        return self.name
    
class Next(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Crd(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.ImageField(upload_to='card', blank=True, null=True)
    file = models.FileField(upload_to='file/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'doc'])], help_text="Faqat PDF, DOCX yoki DOC fayllarni yuklang.")
    button = models.CharField(max_length=100)

    def __str__(self):
        return self.name