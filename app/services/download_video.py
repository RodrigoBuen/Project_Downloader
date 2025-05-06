from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress
import os, shutil, time
from pathlib import Path

pasta_atual = Path(".").resolve()

url = ''

class Download_Video():
    def __init__(self):
        self.escolha()

    def download_video(self):
        self.yt = YouTube(url, on_progress_callback=on_progress)
        print(self.yt.title)
        
        self.ys = self.yt.streams.get_highest_resolution()
        self.ys.download()
        
        if os.path.isdir(f'{pasta_atual}/Videos'):
                shutil.move(f'{pasta_atual}/{self.yt.title}.mp4', f'{pasta_atual}/Videos/{self.yt.title}.mp4')
                print('\n Movido com sucesso')
                
        else:
            os.mkdir(f'{pasta_atual}/Videos')
            time.sleep(1)
            print('Pasta criada com sucesso')
            shutil.move(f'{pasta_atual}/{self.yt.title}.mp4', f'{pasta_atual}/Videos/{self.yt.title}.mp4')
            print('\n Movido com sucesso')

        

    def download_playlist(self):
        self.playlist = Playlist(url)
        for self.video in self.playlist.videos:
            print(self.video.title)
            
            ys = self.video.streams.get_highest_resolution()
            ys.download()
            print('\n Completo!!!')
            
            if os.path.isdir('Videos'):
                shutil.move(f'{pasta_atual}/{self.video.title}.mp4', f'{pasta_atual}/Videos/{self.video.title}.mp4')
                print('Movido com sucesso')
                
            else:
                os.mkdir('Videos')
                time.sleep(1)
                print('Pasta criada com sucesso')
                shutil.move(f'{pasta_atual}/{self.video.title}.mp4', f'{pasta_atual}/Videos/{self.video.title}.mp4')
                print('Movido com sucesso')

    def escolha(self):
        if 'www.youtube.com/watch' in url and not 'list=' in url:
            self.download_video()
            print('Download Completo')
        
        elif 'www.youtube.com/watch' in url and 'list=' in url:
            self.download_playlist()
            print('Download Completo')