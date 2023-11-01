from django.db import models

# Create your models here.


class Event_Model(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    post_date = models.DateField()
    pic = models.ImageField(upload_to ='event_photo/', blank= True, null= True)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title
