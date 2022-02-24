from googlesearch import search
import youtube_dl
from time import sleep

campo_entry = ''

class Download_nome():
    def __init__(self):
        self.pesquisa()
        self.run()
        sleep(1)

    def pesquisa(self):
        self.links = []
        for self.musica in search(campo_entry +' lyrics youtube', stop=1):
            if 'https://www.youtube.com/watch' in self.musica:
                self.links.append(self.musica)
                print(self.musica)

    def run(self):
        self.video_url = self.links[0]
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