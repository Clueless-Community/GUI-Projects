from TTS import *
import speech_recognition as sr
import pyaudio 
import pywhatkit as pwt
from Clicker import *
from VideoDownloader import *
from speech_recognition import *

def stt():
    r = sr.Recognizer()
    while True:
        with sr.Microphone(device_index=2) as source:
            # audio_text=r.adjust_for_ambient_noise(source,5)
            # audio=r.listen(source=source,phrase_time_limit=5)
            print("Speech to text : ")
            audio = r.listen(source)
            try:
            # using google speech recognition
                text = r.recognize_google(audio)
                print(text)
                t=pwt.playonyt(text)
                print(t)
                return
            except:
                tts('Couldnt Recognize your voice')
                return

def rstt():
    r = sr.Recognizer()
    while True:
        with sr.Microphone(device_index=2) as source:
            # audio_text=r.adjust_for_ambient_noise(source,5)
            # audio=r.listen(source=source,phrase_time_limit=5)
            print("Speech to text : ")
            audio = r.listen(source)
            try:
            # using google speech recognition
                text = r.recognize_google(audio)
                # print(text)
                return text
            except:
                tts('Couldnt Recognize your voice')
                return ""

def playvideo(video):
    pwt.playonyt(video)