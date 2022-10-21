from MessageSend import *
from TTS import *
import re

def whatsappchecksend(phno,msg):
    phnopattern=re.compile(r"\d{10}")
    matches=phnopattern.findall(phno)
    if matches==[]:
        tts("Invalid Phone Number")
        print("Invalid Phone Number")
    elif msg=="":
        tts("No Message!!")
        print("No Message!!")
    else:
        matches[0]="+91"+matches[0]
        print(matches[0])
        whatsappmsg(matches[0],msg)
