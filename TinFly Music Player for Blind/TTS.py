from gtts import gTTS 
import os 
import time
import pyttsx3  

def rtts(filename):
    fh = open(filename, "r")
    myText = fh.read()#.replace("\n", " ")
    # Language we want to use 
    language = 'en'
    output = gTTS(text=myText, lang=language, slow=False)
    output.save("output.mp3")
    fh.close() 
    os.system("start output.mp3")
    
def tts(text):
    # initialize Text-to-speech engine  
    engine = pyttsx3.init()  
    voices = engine.getProperty('voices')
    engine.setProperty("rate", 178)
    engine.setProperty('voice', voices[1].id) #changing index changes voices but ony 0 and 1 are working here
    # convert this text to speech  
    engine.say(text)  
    # play the speech  
    engine.runAndWait()  
    
# def tts(text):
#     mytext = text
#     language = 'en'
#     myobj = gTTS(text=mytext, lang=language, slow=False) 
#     myobj.save("output.mp3")
#     os.system("start output.mp3") 

# def deletefile(filename):
#     time.sleep(2)
#     os.remove(filename)