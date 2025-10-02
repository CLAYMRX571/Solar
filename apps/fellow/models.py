from django.db import models
from django.core.validators import FileExtensionValidator

class Fellow(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    title = models.TextField()
    
    def __str__(self):
        return self.name
    
class Well(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.ImageField(upload_to='fellow/', blank=True, null=True)

    def __str__(self):
        return self.name

class Lars(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.ImageField(upload_to='lars/', blank=True, null=True)

    def __str__(self):
        return self.name

class Gallery(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Photo(models.Model):
    image = models.ImageField(upload_to='collega/', blank=True, null=True)

    def __str__(self):
        return self.image
    
class Cent(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    title = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Run(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    file = models.FileField(upload_to='file/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'doc'])], help_text="Faqat PDF, DOCX yoki DOC fayllarni yuklang.")

    def __str__(self):
        return self.name