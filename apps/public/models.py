from django.db import models
from django.core.validators import FileExtensionValidator

class Public(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    topic = models.TextField()
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Pub(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.ImageField(upload_to='image', blank=True, null=True)
    file = models.FileField(upload_to='file', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'doc'])], help_text="Faqat PDF, DOCX yoki DOC fayllarni yuklang.")

    def __str__(self):
        return self.name