from django.db import models
from django.core.validators import FileExtensionValidator

class Young(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Fol(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Met(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    file = models.FileField(upload_to='file', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'doc'])], help_text="Faqat PDF, DOCX yoki DOC fayllarni yuklang.")
    button = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Pic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Gal(models.Model):
    image = models.ImageField(upload_to='young', blank=True, null=True)
    
    def __str__(self):
        return self.image
