from django.db import models
from django.core.validators import FileExtensionValidator

class Event(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    area = models.CharField(max_length=200)
    part = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Text(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Greeb(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    file = models.FileField(upload_to='file', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'doc'])], help_text="Faqat PDF, DOCX yoki DOC fayllarni yuklang.")
    button = models.CharField(max_length=50)
    image = models.ImageField(upload_to='event', blank=True, null=True)

    def __str__(self):
        return self.name