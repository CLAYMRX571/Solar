from django.db import models

class Banner(models.Model):
    name = models.CharField(max_length=255)
  
    def __str__(self):
        return self.name
    
class Home(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='itm/', blank=True, null=True)
    desc = models.TextField()
    button_name = models.CharField(max_length=100)
    buttons_name = models.CharField(max_length=100)
    buttons_image = models.ImageField(upload_to='home', blank=True, null=True)
    buttons_desc = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Latest(models.Model):
    category_name = models.CharField(max_length=100)
    browse_link_name = models.CharField(max_length=100)
    latest_image = models.ImageField(upload_to='latest', blank=True, null=True)
    latest_title = models.CharField(max_length=200)
    latest_date = models.DateTimeField(auto_now_add=True)
    latest_desc = models.TextField()

    def __str__(self):
        return self.category_name
    
    def __str__(self):
        return self.latest_date.strftime("%d-%m-%y")