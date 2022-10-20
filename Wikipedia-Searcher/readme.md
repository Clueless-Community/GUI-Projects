# Wikipedia Search GUI
This project is a part of [Global Hack Week (GHW)-INIT 2023](https://organize.mlh.io/participants/events/7950-global-hack-week-init-2023).
- A GUI made in Python which search provided input term (input can be **voice** or **text**) and shows summary.
- We can also listen the summary.
- We can also convert the summary into audio file.
- This GUI is made using tkinter library.

## Original Repo link [🔗](https://github.com/Param302/wikipedia_searcher)


## Demo Video [🔗](https://youtu.be/ltYkbAh_8FU)

![Preview Img](assets/preview.jpg)


## Contributors
- [Anant Luthra](https://github.com/AnantLuthra)
- [Parampreet Singh](https://github.com/Param302)

### Clone this repository
```
git clone https://github.com/AnantLuthra/wikipedia_searcher.git
```


## Softwares & libraries used
- Python 3.10.2
- gTTS==2.2.4
- Pillow==9.2.0
- pyttsx3==2.90
- SpeechRecognition==3.8.1
- ttkbootstrap==1.8.0
- Wikipedia-API==0.5.4
- Pyaudio 0.2.11 (wheel file)

### Setup
1. Make sure to install required modules before using below command:

```$ pip install -r requirements.txt```

And must install `pyaudio` from the provided wheel file in assets folder.

```$ pip install assets\PyAudio-0.2.11-cp310-cp310-win_amd64.whl```

2. Run any of the following commands to use:

```$ python wikipedia_searcher```

Or open [wikipedia_searcher](../wikipedia_searcher/) directory and run

```$ python .```

Or

```$ python gui.py```

3. Enjoy!

