from django.db import models
from django.core.validators import FileExtensionValidator

class Jobs(models.Model):
    name = models.CharField(max_length=255)
    deadline = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Abs(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return self.name
    
class Res(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return self.name
    
class Look(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return self.name
    
class Offer(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return self.name
    
class Apply(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return self.name
    
class Info(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    mail = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Foot(models.Model):
    desc = models.TextField()
    button = models.CharField(max_length=200)
    file = models.FileField(upload_to='file/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'doc'])], help_text="Faqat PDF, DOCX yoki DOC fayllarni yuklang.")

    def __str__(self):
        return self.desc