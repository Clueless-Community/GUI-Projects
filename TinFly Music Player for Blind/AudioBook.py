from TTS import *
import os
from tkinter import filedialog

def ebookreader():
    file= filedialog.askopenfilename(title="Select a PDF", filetype=(("PDF    Files","*.pdf"),("All Files","*.*")))
    print(file)
    os.startfile(file)