import os
import subprocess

def convert_480p(source):

  dir_path, file_name = os.path.split(source)  # Teile den Pfad und den Dateinamen auf
  source= dir_path + '/' + file_name
  print('Source ', source)
  name_only, ext = os.path.splitext(file_name)  # Teile den Dateinamen und die Erweiterung auf
  new_name = name_only + '_480p' + ext  # Neuen Namen erstellen
  target = os.path.join(dir_path, new_name)  # Ziel-Pfad erstellen
  print('Pfad ', target)


  cmd = 'ffmpeg -i "{}" -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source,target) #Command
  print('Command ', cmd)
  subprocess.run(cmd, capture_output=True) #Run command

  
 