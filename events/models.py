from django.db import models

# Create your models here.
class Event(models.Model):
    the_image=models.ImageField(upload_to="event_images/")
    the_text=models.CharField(max_length=300)
