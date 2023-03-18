import os
from .models import Video
from content.tasks import convert_480p
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
import django_rq
from django_rq import enqueue

@receiver(post_save, sender=Video)
def video_post_save(sender, instance, created, **kwargs):
  """
  Video is saved to filesystem
  """
  print('Video was saved')
  if created:
    print('Pfad ',instance.video_file.path)
    queue = django_rq.get_queue('default', autocommit=True) #Unsere einzige QueQue ist 'default' und für fügen Dinge in die Schlange ohne Bestätigung direkt hinzu (autocommit=true)
    queue.enqueue(convert_480p, instance.video_file.path) #Für fügen unsere Konvertierungsfunktion der Schlange hinzu
    #convert_480p(instance.video_file.path) #Video is converted to 480p when created
    print('Video was created')


@receiver(post_delete, sender=Video)
def video_post_delete(sender, instance, using, **kwargs):
  """
  Video gets deleted from filesystem, if corresponding object is deleted
  """
  if instance.video_file:
    if os.path.isfile(instance.video_file.path):
      print(instance.video_file.path) #Path of the video_file
      os.remove(instance.video_file.path) #Video gets deleted
      print('Video was deleted')

#Verknüpft Funktion mit Model und den Zeitpunkt der Ausführung
#post_save (nach dem speichern)
#post_delete (nach dem löschen)
#pre_save (vor dem Speichern)
#pre_delete (vor dem löschen)
#post_save.connect(video_post_save, sender=Video)