from pytube import YouTube, Playlist

url = ''

class Download_Video():
    def __init__(self):
        self.tratativa()

    def download_video(self):
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        print(video)
        video.download()

    def download_playlist(self):
        playlist = Playlist(url)
        for item in playlist:
            yt = YouTube(item)
            video = yt.streams.get_highest_resolution()
            print(video)
            video.download(output_path='playlist')

    def tratativa(self):
        if 'https://www.youtube.com/watch' in url:
            self.download_video()
            print('Download Completo')

        elif 'https://www.youtube.com/playlist' in url:
            self.download_playlist()
            print('Download Completo')
