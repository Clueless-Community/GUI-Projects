from TTS import *
import os
from tkinter import filedialog

def musicfileopen():
    file= filedialog.askopenfilename(title="Select a PDF", filetype=(("All Files","*.*"),("MP3    Files","*.mp3"),("MP4    Files","*.mp4"),("WAV    Files","*.wav")))
    print(file)
    os.startfile(file)