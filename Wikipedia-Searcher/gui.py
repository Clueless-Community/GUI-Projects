import os
from gtts import gTTS
from wiki import Wiki
from voice import DoVoice
import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style, ScrolledText
from PIL import ImageTk, Image

__all__ = ["GUI"]

path = os.getcwd()
path += "/wikipedia_searcher" if "wikipedia_searcher" not in path else ""
IMG_PATH = f"{path}/assets"


class GUI(tk.Tk):

    def __init__(self):
        super().__init__(sync=True)
        self._gui_configs()

    def _gui_configs(self):
        self.title("Wikipedia Searcher")
        self.icon = ImageTk.PhotoImage(Image.open(f"{IMG_PATH}/ws-logo.ico"))
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"1000x800+{screen_width//4}+100")
        self.style = Style(theme="morph")
        self.font = ["Rockwell", 30]
        self.search_wiki = Wiki()
        self.voice = DoVoice()

    def _header(self):
        self._header_frame = ttk.Frame(self, style="primary.TFrame")
        self._app_name = ttk.Label(self._header_frame, text="Wikipedia Searcher",
                                   font=self.font+["bold"], style="primary.inverse.TLabel")
        self._app_name.pack(side="top", anchor="center")

        self._search_frame = ttk.Frame(
            self._header_frame, style="primary.TFrame")
        self.font[1] = 18
        self.name = tk.StringVar()
        self._search_bar = ttk.Entry(self._search_frame, text=self.name,
                                     font=self.font, style="warning.TEntry", width=20)
        self._search_bar.pack(side="left", anchor="center", pady=10, expand=1)

        self.vc_img = ImageTk.PhotoImage(
            Image.open(f"{IMG_PATH}/voice_off.png").resize((26, 27))
        )
        self._voice_btn = ttk.Button(
            self._search_frame, image=self.vc_img, style="primary.TButton", command=self.listen)
        self._voice_btn.pack(side="left", expand=1)

        self.search_img = ImageTk.PhotoImage(
            Image.open(f"{IMG_PATH}/search.png").resize((26, 27))
        )
        self._search_btn = ttk.Button(
            self._search_frame, image=self.search_img, style="primary.TButton", command=self.search)
        self._search_btn.pack(side="left", expand=1)

        self._search_frame.pack(side="top", anchor="center")
        self._header_frame.pack(side="top", fill="x", anchor="n")

    def _show_text(self):
        self._main_frame = ttk.Frame(self, style="primary.TFrame")
        self.font[1] = 14
        self.text_area = ScrolledText(self._main_frame, font=self.font,
                                      height=20, state="disabled")
        self.text_area.pack(side="top", anchor="center",
                            fill="x", padx=150, pady=20)
        self.text_area.configure(font=self.font)
        self.speak_img = ImageTk.PhotoImage(
            Image.open(f"{IMG_PATH}/speak.png").resize((50, 50))
        )
        self._speak_btn = ttk.Button(self._main_frame, text="Speak text",
                                     image=self.speak_img, compound="top",
                                     style="warning.TButton", command=self.speak)
        self._speak_btn.pack(side="top")

        self.audio_img = ImageTk.PhotoImage(
            Image.open(f"{IMG_PATH}/audio-file.png").resize((50, 50))
        )
        self._convert_audio_btn = ttk.Button(self._main_frame, text="Convert text to Audio file",
                                             image=self.audio_img, compound="top", style="success.TButton",
                                             command=self.convert_audio)
        self._convert_audio_btn.pack(side="top", pady=20)

        self._main_frame.pack(side="top", fill="both", expand=1)

    def listen(self):
        name = self.voice.take_voice()
        self.name.set(name)

    def search(self):
        text = self.search_wiki.search_wiki(self.name.get())

        self.text_area.delete("1.0", "end")

        self.text_area.configure(state="normal")
        self.text_area.insert("0.0", text)
        self.text_area.configure(state="disabled")

    def speak(self):
        self.voice.speak(self.text_area.get("0.0", tk.END))

    def convert_audio(self):
        text = self.text_area.get("0.0", tk.END)
        myobj = gTTS(text=text, lang="en", slow=False)
        myobj.save(f"{IMG_PATH.replace('/assets/', '')}./audio.mp3")

    def run(self):
        self._header()
        self._show_text()
        self.mainloop()


if __name__ == "__main__":
    mygui = GUI()
    mygui.run()
