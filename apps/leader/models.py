from django.db import models
from django.core.validators import FileExtensionValidator

class Leader(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    image = models.ImageField(upload_to='leader/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Cont(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    image = models.ImageField(upload_to='leaders/', blank=True, null=True)

    def __str__(self):
        return self.name

class Win(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    file = models.FileField(upload_to='file/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'doc'])], help_text="Faqat PDF, DOCX yoki DOC fayllarni yuklang.")

    def __str__(self):
        return self.name