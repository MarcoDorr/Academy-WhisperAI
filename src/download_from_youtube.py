import os

import yt_dlp
from yt_dlp import YoutubeDL


def get_audio(url):
    with YoutubeDL() as ydl:
        info_dict = ydl.extract_info(url, download=False)
        video_url = info_dict.get("url", None)
        video_id = info_dict.get("id", None)
        video_title = info_dict.get('title', None)

    temp_dir = f'../xentral_sample_videos_anwendertraining/'

    ydl = yt_dlp.YoutubeDL({
        'quiet': True,
        'verbose': False,
        'format': 'bestaudio',
        "outtmpl": os.path.join(temp_dir, f"{video_title}.%(ext)s"),
        'postprocessors': [
            {'preferredcodec': 'mp3', 'preferredquality': '192', 'key': 'FFmpegExtractAudio', }],
    })

    ydl.extract_info(url, download=True)


if __name__ == '__main__':
    url1 = 'https://www.youtube.com/watch?v=uQb5CkDillA'
    get_audio(url1)
