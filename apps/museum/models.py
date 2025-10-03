from django.db import models
from django.core.validators import FileExtensionValidator

class Museum(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Ms(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.ImageField(upload_to='img', blank=True, null=True)
    file = models.FileField(upload_to='file/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'doc'])], help_text="Faqat PDF, DOCX yoki DOC fayllarni yuklang.")
    button = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Mega(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Gall(models.Model):
    image = models.ImageField(upload_to='museum', blank=True, null=True)

    def __str__(self):
        return self.image

class Supa(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    file = models.FileField(upload_to='file/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'doc'])], help_text="Faqat PDF, DOCX yoki DOC fayllarni yuklang.")
    button = models.CharField(max_length=100)

    def __str__(self):
        return self.name