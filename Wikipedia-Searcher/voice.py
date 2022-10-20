import pyttsx3
import speech_recognition as sr


class DoVoice:

    """This DoVoice class is for voice related function."""

    def take_voice(self) -> str:
        """
        This function returns a string taking input from the user's microphone.
        """

        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            self.speak("Listening")
            audio = r.listen(source)

        try:
            query = r.recognize_google(audio, language="en-in")
            return query  #Returning string said by user.

        except Exception as e:
            return e
    

    @staticmethod
    def speak(string:str) -> None:
        """
        This function speaks the give string.
        """
        # Code for tuning voice of assistant into a famale voice...

        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)

        engine.say(string)
        engine.runAndWait()
    