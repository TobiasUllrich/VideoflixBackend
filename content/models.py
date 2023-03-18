from django.db import models
from django.contrib.auth.models import User
from datetime import date

# [1.] Model User already exists (id, username,first_name,last_name,email,password)

# [2.] Videos (id, video_title, video_description, video_created_at, video_file)
class Video(models.Model):
    video_title = models.CharField(max_length=80)
    video_description = models.CharField(max_length=500)
    video_created_at = models.DateField(default=date.today)
    video_file = models.FileField(upload_to='videos',blank=True,null=True) #Upload in videos-Ordner, Feld kann leer oder null sein
    #Langfristig wird so ein Video-Ordner eher in ein CDN (Content-Delivery-Network) ausgelagert