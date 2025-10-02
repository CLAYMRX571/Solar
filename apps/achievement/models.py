from django.db import models
from django.core.validators import FileExtensionValidator

class Achievement(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    
    def __str__(self):
        return self.name
    
class Recept(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.ImageField(upload_to='achieve/', blank=True, null=True)
   
    def __str__(self):
        return self.name
    
class Past(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    file = models.FileField(upload_to='file/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'doc'])], help_text="Faqat PDF, DOCX yoki DOC fayllarni yuklang.")

    def __str__(self):
        return self.name