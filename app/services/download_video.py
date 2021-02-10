from pytube import YouTube, Playlist
import os
import prefs

url = ''
path = 'C:' + os.sep + 'Users' + os.sep + f'{prefs.Computador_nome}' + os.sep + 'Downloads'

class Download_Video():
    def __init__(self):
        self.tratativa()

    def download_video(self):
        yt = YouTube(url)
        if yt.streams.filter(resolution='720p', progressive='True'):
            video = yt.streams.first()
            print(video)
            video.download(path)
        elif yt.streams.filter(resolution='480p', progressive='True'):
            video = yt.streams.first()
            print(video)
            video.download(path)
        elif yt.streams.filter(resolution='360p', progressive='True'):
            video = yt.streams.first()
            print(video)
            video.download(path)

    def download_playlist(self):
        playlist = Playlist(url)
        for item in playlist:
            yt = YouTube(item)
            if yt.streams.filter(resolution='720p', progressive='True'):
                video = yt.streams.first()
                print(video)
                video.download(path, output_path='playlist')
            elif yt.streams.filter(resolution='480p', progressive='True'):
                video = yt.streams.first()
                print(video)
                video.download(path, output_path='playlist')
            elif yt.streams.filter(resolution='360p', progressive='True'):
                video = yt.streams.first()
                print(video)
                video.download(path, output_path='playlist')

    def tratativa(self):
        if 'https://www.youtube.com/watch' in url:
            self.download_video()
            print('Download Completo')

        elif 'https://www.youtube.com/playlist' in url:
            self.download_playlist()
            print('Download Completo')
