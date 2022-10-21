from pytube import YouTube
from tkinter import filedialog
from TTS import tts

def videodownload(link,filepath):
    my_video = YouTube(link)
    my_video = my_video.streams.get_highest_resolution()
    my_video.download(output_path=filepath)
    print("Download Complete")
    tts("Download Complete")