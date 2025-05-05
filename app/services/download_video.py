from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress

url = ''

class Download_Video():
    def __init__(self):
        self.escolha()

    def download_video(self):
        yt = YouTube(url, on_progress_callback=on_progress)
        print(yt.title)
        
        ys = yt.streams.get_highest_resolution()
        ys.download()
        

    def download_playlist(self):
        playlist = Playlist(url)
        for video in playlist.videos:
            print(video.title)
            
            ys = video.streams.get_highest_resolution()
            ys.download()
            print('\n Completo!!!')

    def escolha(self):
        if 'www.youtube.com/watch' in url and not 'list=' in url:
            self.download_video()
            print('Download Completo')

        elif 'www.youtube.com/watch' in url and 'list=' in url:
            self.download_playlist()
            print('Download Completo')
