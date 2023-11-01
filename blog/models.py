from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class BlogModel(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    body = HTMLField()
    pic = models.ImageField(upload_to='blog_photo/', blank=True, null=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
