import youtube_dl
import os
import shutil
import prefs
from time import sleep

campo_entry = ''
path = 'C:' + os.sep + 'Users' + os.sep + f'{prefs.Computador_nome}' + os.sep + 'Downloads'
path2 = 'C:'+os.sep+'Users'+os.sep+f'{prefs.Computador_nome}'+os.sep+'OneDrive'+os.sep+'Área de Trabalho'+os.sep+'Music_Download'

class Download_link():
    def __init__(self):
        self.run()
        sleep(2)
        self.move()

    def run(self):
        self.video_url = campo_entry
        self.video_info = youtube_dl.YoutubeDL().extract_info(
            url=self.video_url, download=False)

        self.filename = f"{self.video_info['title']}.mp3"

        self.options = {
            'format': 'bestaudio / best',
            'keepvideo': False,
            'outtmpl': self.filename,
            'postprocessors': [{'key': 'FFmpegExtractAudio',
                                'preferredcodec': 'mp3',
                                'preferredquality': '256', }]
        }

        try:
            with youtube_dl.YoutubeDL(self.options) as ydl:
                ydl.download([self.video_info['webpage_url']])

        except:
            print('Baixada com sucesso')

    def move(self):
        os.chdir(path2)
        shutil.move(f'{self.filename}', path + os.sep + f'{self.filename}')