import calendar
from django.db import models
from django.core.validators import FileExtensionValidator

class Column(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return self.name

class Data(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Mons(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    file = models.FileField(upload_to='file', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'doc'])], help_text="Faqat PDF, DOCX yoki DOC fayllarni yuklang.")
    
    def month_year(self) -> str:
        return f"{calendar.month_name[self.date.month]} {self.date.year}"