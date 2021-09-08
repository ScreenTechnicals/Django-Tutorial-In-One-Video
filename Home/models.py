from django.db import models

# Create your models here.

# Post model
class Post(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()
    imgae_url = models.TextField()
    image = models.ImageField(upload_to="images", default="")
    slug = models.CharField(max_length=50, default="")
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=250)
    purpose = models.TextField()
    def __str__(self):
        return self.username
