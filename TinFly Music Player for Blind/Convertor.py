from moviepy.editor import *

def convertor(inputfile,convertedfile):
    mp4_file = inputfile
    mp3_file = convertedfile

    videoclip = VideoFileClip(mp4_file)
    
    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file)
    
    audioclip.close()
    videoclip.close()