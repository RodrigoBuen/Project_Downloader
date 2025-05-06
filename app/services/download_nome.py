from googlesearch import search
from pytubefix import YouTube
from pytubefix.cli import on_progress
from moviepy import *
from time import sleep
import os, shutil
from pathlib import Path

# Definindo o caminho raiz
pasta_atual = Path(".").resolve()

campo_entry = ''

class Download_nome():
    def __init__(self):
        self.pesquisa()
        self.run()
        self.move_create()

    def pesquisa(self):
        self.links = []
        for self.musica in search(campo_entry +' lyrics youtube', stop=1):
            if 'https://www.youtube.com/watch' in self.musica:
                self.links.append(self.musica)
                print(self.musica)

    def run(self):
        self.video_url = self.links[0]
        self.url_extractor = YouTube(self.video_url, on_progress_callback=on_progress)
        print(self.url_extractor.title)

        try:
            self.ys = self.url_extractor.streams.get_audio_only()
            self.ys.download()
            sleep(2)
            
            self.audio_a4 = AudioFileClip(f'{self.url_extractor.title}.m4a')
            print('\n arquivo encontrado')
            
            self.audio_a4.write_audiofile(f'{self.url_extractor.title}.mp3')
            print('\n convertido com sucesso')
            
            os.remove(f'{pasta_atual}/{self.url_extractor.title}.m4a')
            print('\n deletado com sucesso')
            

        except:
            print('Baixada com sucesso')
            
    def move_create(self):
        if os.path.isdir('Musicas'):
            shutil.move(f'{pasta_atual}/{self.url_extractor.title}.mp3', f'{pasta_atual}/Musicas/{self.url_extractor.title}.mp3')
            print('Movido com sucesso')
            
        else:
            os.mkdir('Musicas')
            sleep(1)
            print('Pasta criada com sucesso')
            shutil.move(f'{pasta_atual}/{self.url_extractor.title}.mp3', f'{pasta_atual}/Musicas/{self.url_extractor.title}.mp3')
            print('Movido com sucesso')