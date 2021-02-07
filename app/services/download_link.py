import youtube_dl

campo_entry = ''

class Download_link():
    def __init__(self):
        self.run()

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