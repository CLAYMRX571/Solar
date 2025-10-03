from django.db import models
from django.urls import reverse
from django.core.validators import FileExtensionValidator

class News(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class New(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    button = models.CharField(max_length=100)
    file = models.FileField(upload_to='file', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'doc'])], help_text="Faqat PDF, DOCX yoki DOC fayllarni yuklang.")
    image = models.ImageField(upload_to='news', blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("news") 