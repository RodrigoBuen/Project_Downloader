from pytube import YouTube, Playlist
from tkinter.filedialog import asksaveasfile
import os
import prefs

url = ''
path = 'C:' + os.sep + 'Users' + os.sep + f'{prefs.Computador_nome}' + os.sep + 'Downloads'

class Download_Video():
    def __init__(self):
        self.tratativa()

    def download_video(self):
        yt = YouTube(url)
        try:
            video = yt.streams.filter(file_extension='mp4', resolution='720p', video_codec="avc1.64001F", audio_codec="mp4a.40.2").first()
            video.download(path)
            print('Download Completo')
        except:
            video = yt.streams.filter(file_extension='mp4', resolution='480p', video_codec="avc1.64001F", audio_codec="mp4a.40.2").first()
            video.download(path)
            print('Download Completo')

    def download_playlist(self):
        playlist = Playlist(url)
        for item in playlist:
            yt = YouTube(item)
            try:
                video = yt.streams.filter(file_extension='mp4', resolution='720p', video_codec="avc1.64001F", audio_codec="mp4a.40.2").first()
                video.download(path, output_path='playlist')
                print('Download Completo')
            except:
                video = yt.streams.filter(file_extension='mp4', resolution='480p', video_codec="avc1.64001F", audio_codec="mp4a.40.2").first()
                video.download(path, output_path='playlist')
                print('Download Completo')

    def tratativa(self):
        if 'https://www.youtube.com/watch' in url:
            self.download_video()

        elif 'https://www.youtube.com/playlist' in url:
            self.download_playlist()
