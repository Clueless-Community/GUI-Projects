import pywhatkit as pwt
import time,pygame
import sys
from os import listdir
from os.path import isfile, join
from tkinter import filedialog,messagebox,colorchooser, ttk
from tkinter import *
from PIL import ImageTk, Image
from Convertor import *
from PlaySingleMusic import *
from TTS import *
from STT import *
from Clicker import *
from HandDetection import *
from AudioBook import *
from VoiceDraw import *
from VideoDownloader import *
from Whatsapp import *
from mutagen.mp3 import MP3
import random

root=Tk() #main container object
root.title("TinFly")
root.state("zoomed")

volume=0.5

# functions
def sttx():
    tts("Speak Video or Music Title")
    stt()
    
def playvideox():
    tts("Search Button Clicked")
    text= query.get()
    playvideo(text)
    
def gesturesx():
    tts("Gestures Recognition Activated")
    handDetect()

def downloadvideo():
    tts("Video Download")
    text=query.get()
    t=pwt.playonyt(text,open_video=False)
    # print(t)
    file_path = filedialog.askdirectory()
    # print(file_path)
    videodownload(t,file_path)

def googlefun():
    tts("Google Search")
    text=query.get()
    pwt.search(text)

def infofun():
    tts("Information Search")
    text=query.get()
    try:
        draw=pwt.info(text,return_value=True)
        # print("Hi : ",draw)
        tts(draw)
        tdraw(draw)
    except:
        str="No Information about "+text
        tts(str)

def musicPlayerWindow():
    playlistdirname = filedialog.askdirectory()
    playlistfiles = [f for f in listdir(playlistdirname) if isfile(join(playlistdirname, f))]
    playlist=[playlistdirname+'/'+i for i in playlistfiles if i.endswith('.mp4')]
    names=[i[:-4] for i in playlist]
    # print(playlistfiles)
    # for i in names:
    #     print(i)
    convertedsonglist=[]
    j=0
    for i in playlist:
        if os.path.isfile(names[j]+'.mp3')==False:
            convertor(i,names[j]+'.mp3')
            convertedsonglist.append(names[j]+".mp3")
        j+=1
    # for i in playlist:
    #     os.remove(i)
    playlist=[playlistdirname+'/'+i for i in playlistfiles if i.endswith('.mp3')]
    playlist+=convertedsonglist
    random.shuffle(playlist)
    # for i in playlist:
    #     print(i)
    class MusicPlayer:
        def __init__(self, root, backward_img, play_img, pause_img, stop_image_btn, forward_img):
            self.mpWindow = root
            # Some variables initialize with None 
            self.my_list_song = None
            self.mute_scale = None
            self.loop_bar = None
            self.loop_bar = None

            # Some integer variable initialization
            self.loop_change = IntVar()
            self.repeat_change = IntVar()
            self.mute_change = IntVar()
            self.loop_counter = IntVar()
            self.repeat_counter = IntVar()

            # Btn img initialization
            self.forward_btn = forward_img
            self.backward_btn = backward_img
            self.pause_btn = pause_img
            self.play_btn = play_img
            self.stop_btn = stop_image_btn

            # Value initialization
            self.song_duration_bar = 0
            self.song_length = 0
            self.repeat_counter = 1
            self.loop_counter = 0
            self.total_song = 0
            self.loop_status = 1
            self.repeat_status = 1
            self.mute_status = 1

            # pygame initialization
            pygame.mixer.init()

            # Default function calling
            self.basic_setup()
            self.instructional_btn_setup()
            self.image_button_function_set()
            self.song_duration()
            self.muter()
            self.repeat_controller()
            self.loop_controller()
            MusicPlay.bind('<Delete>', self.clear)

            add_multiple_song = playlist
            for song in add_multiple_song:
                self.my_list_song.insert(END, song)
                time.sleep(0.5)
                mpWindow.update()
            
            self.my_list_song.select_set(0)
        def basic_setup(self):
            # Heading
            Label(self.mpWindow,text="TinFly Music Player",justify=CENTER, font=("Arial",20,"bold"),bg="#a449b3",fg="gold").place(x=820,y=25)

            # Song Collection
            frame = Frame(self.mpWindow)
            frame.place(x=25,y=80)

            v_scroll = Scrollbar(frame)
            v_scroll.pack(side=RIGHT, fill=Y)

            self.my_list_song = Listbox(frame, bg="#404040", fg="#ffbf50", width=260, height=25, font=("Arial",8,"bold"), relief=SUNKEN, borderwidth=20, yscrollcommand=v_scroll.set)
            self.my_list_song.pack(side=LEFT, anchor=NW)

            v_scroll.configure(command=self.my_list_song.yview)

        def instructional_btn_setup(self): # Some button initialization
            song_add = Button(self.mpWindow,text="Add Song",relief=RAISED,image=addsongimg, borderwidth=5, command=self.add_song)
            song_add.place(x=1080,y=652)
            songaddtxt=Label(self.mpWindow,text="Add Song",justify='center',font=("Helvetica"))
            songaddtxt.place(x=1080,y=762,width=107) 

            delete_song = Button(self.mpWindow, text="Delete Selected Song", relief=RAISED, image=delsongimg,borderwidth=5,command=self.delete_selected_song)
            delete_song.place(x=1380, y=652)
            deletesongtxt=Label(self.mpWindow,text="Delete Song",justify='center',font=("Helvetica"))
            deletesongtxt.place(x=1380,y=762,width=107) 

            song_counter = Button(self.mpWindow, text="Song Counter", width=13,font=("Helvetica", 15, "bold", "italic"), activebackground="#262626", activeforeground="gold",bg="#a449b3",fg="gold", relief=RAISED, borderwidth=5, command=self.song_counter)
            song_counter.place(x=1650, y=652)

        def image_button_function_set(self):# Instructional buttons
            self.play_btn.config(command=lambda: self.play_song('<Return>'))
            MusicPlay.bind('<Return>',self.play_song)
            self.my_list_song.bind('<Double-Button-1>', self.play_song)

            self.pause_btn.config(command=lambda: self.pause_song('<space>'))
            MusicPlay.bind('<space>',self.pause_song)

            self.stop_btn.config(command=lambda: self.stop_song('<0>'))
            MusicPlay.bind('<Escape>', self.stop_song)

            self.forward_btn.config(command=lambda: self.next_song('<Right>'))
            MusicPlay.bind('<Right>', self.next_song)

            self.backward_btn.config(command=lambda: self.previous_song('<Left>'))
            MusicPlay.bind('<Left>', self.previous_song)

        def add_song(self):# Adding songs
            add_multiple_song = filedialog.askopenfilenames(title="Select one or multiple song",filetypes=(("MP3 files", "*mp3"), ("WAV files","*.wav")))
            for song in add_multiple_song:
                self.my_list_song.insert(END, song)
                time.sleep(0.5)
                self.mpwindow.update()

        def delete_selected_song(self):# Delete a particular song
            self.stop_song()
            self.my_list_song.delete(ACTIVE)

        def song_counter(self):# Total song present in the list
            messagebox.showinfo("Song Counter", "Total song in the list: " + str(self.my_list_song.size()))

        def song_duration(self):# Make Song_Duration Label
            self.song_duration_bar = Label(self.mpWindow, text="Song Duration", font=("Arial",17,"bold"), fg="white", bg="#141414",width=25)
            self.song_duration_bar.place(x=780, y=550)    

        global occurencesong
        occurencesong=0
        
        def play_song(self,e=None):# Play a song
            try:
                # Song Load and Play
                take_selected_song = self.my_list_song.get(ACTIVE)
                # print(take_selected_song)
                pygame.mixer.music.load(take_selected_song)
                pygame.mixer.music.play(loops=self.repeat_counter)

                # Song length find
                global song_type
                song_type = MP3(take_selected_song)
                self.song_length = time.strftime("%H:%M:%S", time.gmtime(song_type.info.length))
                

                # Song Duration Label Position Set and Song Duration Function call
                self.song_duration_bar.place(x=780,y=550)
                slider_position=int(song_type.info.length)
                slider.config(to=slider_position,value=0)
                global occurencesong
                occurencesong+=1
                if occurencesong==1:
                    self.song_duration_time()
            except Exception as e:
                print(e)
                tts("Error in play song")
                print("\nError in play song")
                self.next_song()

        def slideplaysong(self):
            take_selected_song = self.my_list_song.get(ACTIVE)
            pygame.mixer.music.load(take_selected_song)
            pygame.mixer.music.play(loops=self.repeat_counter,start=int(slider.get()))
            
        def song_duration_time(self):# Song duration time controller
            try:
                i=0
                global occurencesong
                raw_time=[]
                musicpos = pygame.mixer.music.get_pos()/1000
                raw_time.append(musicpos)
                # print(raw_time)
                converted_time = time.strftime("%H:%M:%S",time.gmtime(raw_time[i]))
                # print("I",i)
                # print("Self Song",self.song_length)
                # print("converted Time",converted_time)
                if (self.song_length == converted_time  and self.repeat_counter == 1) or converted_time=="23:59:59":
                    i+=1
                    occurencesong=0
                    self.next_song()
                elif (self.song_length == converted_time and self.repeat_counter == -1) or converted_time=="23:59:59":
                    # print("Repeat Enter")
                    slider_position=int(song_type.info.length)
                    slider.config(to=slider_position,value=0)
                    i+=1
                    occurencesong=0
                    # self.song_duration_bar.config(text="Time is: "+str(converted_time)+" of "+str(self.song_length))
                    self.play_song()
                else: 
                    # raw_time[i]+=1
                    if int(slider.get())==int(raw_time[i]+1):
                        #slider has not moved
                        # i+=1
                        slider_position=int(song_type.info.length)
                        slider.config(to=slider_position,value=int(raw_time[i]))
                        self.song_duration_bar.config(text="Time is: "+str(converted_time)+" of "+str(self.song_length))
                    else:
                        #slider has been moved
                        slider_position=int(song_type.info.length)
                        slider.config(to=slider_position,value=int(slider.get()))
                        converted_time = time.strftime("%H:%M:%S",time.gmtime(slider.get()))
                        self.song_duration_bar.config(text="Time is: "+str(converted_time)+" of "+str(self.song_length))
                        
                        if (self.song_length == converted_time and self.repeat_counter == -1) or converted_time=="23:59:59":
                            print("Repeat Enter")
                            slider_position=int(song_type.info.length)
                            slider.config(to=slider_position,value=0)
                            i+=1
                            occurencesong=0
                            # self.song_duration_bar.config(text="Time is: "+str(converted_time)+" of "+str(self.song_length))
                            # self.play_song()
                            
                        next_time=int(slider.get())+1
                        slider.config(value=next_time)
                    
                    i+=1
                    self.song_duration_bar.after(1000,self.song_duration_time)# Recursive function call after 1 sec = 1000ms
            except Exception as e:
                # print(i)
                # print(raw_time)
                # print(e)
                tts("Error in song duration")
                print("Error in song duration")        
                self.next_song()
             
        def pause_song(self,e=None):
            pygame.mixer.music.pause()
            self.pause_btn.config(command=self.play_after_pause)
            MusicPlay.bind('<space>', self.play_after_pause)

        def play_after_pause(self,e=None):# Play the song after pause
            pygame.mixer.music.unpause()
            self.pause_btn.config(command=self.pause_song)
            MusicPlay.bind('<space>', self.pause_song)
        
        global stopped
        stopped=False
        
        def stop_song(self,e=None):# Stop playing song
            pygame.mixer.music.stop()
            self.song_duration_bar.destroy()
            self.song_duration()
            
            global stopped
            stopped=True

        def next_song(self,e=None):# Next song control
            try:
                current_song = self.my_list_song.curselection()
                self.my_list_song.selection_clear(ACTIVE)
                current_song = current_song[0]+1

                if current_song < self.my_list_song.size():
                    self.my_list_song.selection_set(current_song)
                    self.my_list_song.activate(current_song)
                    slider_position=int(song_type.info.length)
                    slider.config(to=slider_position,value=0)
                    self.play_song()

                elif self.loop_counter == 0:
                    self.stop_song()

                else:
                    self.my_list_song.selection_set(0)
                    self.my_list_song.activate(0)
                    slider_position=int(song_type.info.length)
                    slider.config(to=slider_position,value=0)
                    self.play_song()
            except:
                tts("Error in next song")
                print("Error in next song")
                pass

        def previous_song(self,e=None):# Previous song control
            try:
                song = self.my_list_song.curselection()
                self.my_list_song.selection_clear(ACTIVE)
                song = song[0]-1

                if song>-1:
                    self.my_list_song.activate(song)
                    self.my_list_song.selection_set(song)
                    self.play_song()

                elif self.loop_counter ==0:
                    self.stop_song()

                else:
                    self.my_list_song.selection_set(0)
                    self.my_list_song.activate(0)
                    self.play_song()
            except:
                tts("Error in previous song")
                print("\nError in previous song")
                pass

        def muter(self):# Mute set-up
            self.mute_scale = Scale(self.mpWindow,from_=1,to=0,orient=HORIZONTAL,bg="#9f9fff",command=self.get_mute, activebackground="red",font=("Arial",15,"bold"),length=47,relief=RIDGE,bd=3)
            self.mute_scale.place(x=25,y=647)

            self.mute_scale.set(self.mute_status)

            mute_indicator = Label(self.mpWindow,text="Mute",font=("Arial",10,"bold"),fg="blue",bg="#9f9fff")
            mute_indicator.place(x=35,y=652)

        def get_mute(self,indicator):# Mute functionality
            pygame.mixer.music.set_volume(int(indicator))
            if int(indicator)==1:
                self.mute_change.set(0)
            else:
                self.mute_change.set(1)

        def repeat_controller(self):# Repeat Set-up
            self.loop_bar = Scale(self.mpWindow,from_=1,to=0,orient=HORIZONTAL,bg="#9f9fff",command=self.repeat_maintain, activebackground="red",font=("Arial",15,"bold"),length=170,relief=RIDGE,bd=3)
            self.loop_bar.place(x=135,y=647)

            self.loop_bar.set(self.repeat_status)

            loop_bar_indicator = Label(self.mpWindow,text="Off    Repeat    On",font=("Arial",10,"bold"),fg="blue",bg="#9f9fff")
            loop_bar_indicator.place(x=150,y=652)

        def repeat_maintain(self, indicator):# Repeat functionality
            if int(indicator) == 1:
                self.repeat_counter = 1
                self.repeat_change.set(0)
            else:
                self.repeat_counter = -1
                self.repeat_change.set(1)

            self.mpWindow.update()

        def loop_controller(self):# loop set-up
            self.loop_bar = Scale(self.mpWindow,from_=1,to=0,orient=HORIZONTAL,bg="#9f9fff",command=self.loop_maintain, activebackground="red",font=("Arial",15,"bold"),length=170,relief=RIDGE,bd=3)
            self.loop_bar.place(x=405,y=647)

            self.loop_bar.set(self.loop_status)

            loop_bar_indicator = Label(self.mpWindow,text="  Off      Loop      On",font=("Arial",10,"bold"),fg="blue",bg="#9f9fff")
            loop_bar_indicator.place(x=415,y=652)

        def loop_maintain(self, indicator):# loop functionality
            if int(indicator) ==1:
                self.loop_counter = 0
                self.loop_change.set(0)
            else:
                self.loop_counter = 1
                self.loop_change.set(1)    

        def clear(self, e=None):# Clear the song list
            try:
                self.stop_song()
                self.my_list_song.delete(0, END)
            except:
                tts("Nothing Present", "Song list is empty")
                messagebox.showerror("Nothing Present", "Song list is empty")
    #functions
    def volumeupfun():
        global volume
        volume=volume+0.1
        pygame.mixer.music.set_volume(volume)
        print("Volume Up")
        # currenttime = oldsongtime+change+addedtime

    def volumedownfun():
        global volume
        volume=volume-0.1
        pygame.mixer.music.set_volume(volume)
        print("Volume Down")
        # pygame.mixer.music.set_pos(pygame.mixer.music.get_pos()-5000)
    
    def closewindow():
        Tinfly.stop_song()
        MusicPlay.destroy()
    
    def forwardby5():
        slider.config(value=int(slider.get())+5)
        Tinfly.slideplaysong()
        
    def rewindby5():
        if (int(slider.get())-5)<=0:
            slider.config(value=0)
            Tinfly.slideplaysong()
        else:
            slider.config(value=int(slider.get())-5)
            Tinfly.slideplaysong()
    
    def popout():
        take_selected_song = Tinfly.my_list_song.get(ACTIVE)
        # print(take_selected_song)
        try:
            file=take_selected_song[:-3]+"mp4"
            print(file)
            os.startfile(file)
        except:
            tts("MP4 File Not Found")
    #images
    bgimg = Image.open("Photos/bg.jpg")
    resize_image = bgimg.resize((1920,1024))
    bgimg = ImageTk.PhotoImage(resize_image)
    
    addsongimg = Image.open("Pictures/addsong.png")
    resize_image = addsongimg.resize((100,100))
    addsongimg = ImageTk.PhotoImage(resize_image)
    
    delsongimg = Image.open("Pictures/deletesong.png")
    resize_image = delsongimg.resize((100,100))
    delsongimg = ImageTk.PhotoImage(resize_image)
    
    #gui
    MusicPlay = Toplevel(root)
    MusicPlay.title("TinFly")
    MusicPlay.state("zoomed")
    
    mpWindow = Frame(master=MusicPlay,width=1920,height=1080)
    mpWindow.pack()    
    
    musicbg = Label(master= mpWindow, image = bgimg)
    musicbg.pack()

    #550 x
    popoutimg = ImageTk.PhotoImage(Image.open('Pictures/popout.png').resize((100,100)))
    popoutbtn = Button(mpWindow, image=popoutimg, bg="#323232", activebackground="#323232", relief=RAISED, bd=3,command=popout)
    popoutbtn.place(x=780,y=652)
    popouttxt=Label(master=mpWindow,text="Pop Out",justify='center',font=("Helvetica"))
    popouttxt.place(x=780,y=762,width=107)
    
    volumedown = ImageTk.PhotoImage(Image.open('Pictures/volumedown.png').resize((100,100)))
    volumedownimg = Button(mpWindow, image=volumedown, bg="#323232", activebackground="#323232", relief=RAISED, bd=3,command=volumedownfun)
    volumedownimg.place(x=190,y=825)
    volumedowntxt=Label(master=mpWindow,text="Volume Down",justify='center',font=("Helvetica"))
    volumedowntxt.place(x=190,y=930,width=107)

    backward_image_take = ImageTk.PhotoImage(Image.open('Pictures/backward.png').resize((100,100)))
    backward_btn_img = Button(mpWindow, image=backward_image_take, bg="#323232", activebackground="#323232", relief=RAISED, bd=3)
    backward_btn_img.place(x=370,y=825)
    backward_btntxt=Label(master=mpWindow,text="Previous Song",justify='center',font=("Helvetica"))
    backward_btntxt.place(x=370,y=930,width=107)
    
    decrement5imgtake = ImageTk.PhotoImage(Image.open('Pictures/5decrement.jpg').resize((100,100)))
    decrement5img = Button(mpWindow,image=decrement5imgtake,bg="#323232", activebackground="#323232", relief=RAISED,bd=3,command=rewindby5)
    decrement5img.place(x=550,y=825)
    decrement5txt=Label(master=mpWindow,text="Rewind",justify='center',font=("Helvetica"))
    decrement5txt.place(x=550,y=930,width=107)  
    
    play_image_take = ImageTk.PhotoImage(Image.open('Pictures/play.png').resize((100,100)))
    play_btn_img = Button(mpWindow,image=play_image_take,bg="#323232", activebackground="#323232", relief=RAISED,bd=3)
    play_btn_img.place(x=730,y=825)
    playbtntxt=Label(master=mpWindow,text="Restart",justify='center',font=("Helvetica"))
    playbtntxt.place(x=730,y=930,width=107)

    pause_image_take = ImageTk.PhotoImage(Image.open('Pictures/pause.png').resize((100,100)))
    pause_btn_img = Button(mpWindow,image=pause_image_take,bg="#323232", activebackground="#323232",relief=RAISED,bd=3)
    pause_btn_img.place(x=910,y=825)
    pausebtntxt=Label(master=mpWindow,text="Pause/Play",justify='center',font=("Helvetica"))
    pausebtntxt.place(x=910,y=930,width=107)

    stop_image_take = ImageTk.PhotoImage(Image.open('Pictures/stop_img_is.png').resize((100,100)))
    stop_btn_img = Button(mpWindow,image=stop_image_take,bg="#323232", activebackground="#323232", relief=RAISED,bd=3)
    stop_btn_img.place(x=1090,y=825)
    stopbtntxt=Label(master=mpWindow,text="Stop",justify='center',font=("Helvetica"))
    stopbtntxt.place(x=1090,y=930,width=107)

    #1270 x 
    increment5imgtake = ImageTk.PhotoImage(Image.open('Pictures/5increment.jpg').resize((100,100)))
    increment5img = Button(mpWindow,image=increment5imgtake,bg="#323232", activebackground="#323232", relief=RAISED,bd=3,command=forwardby5)
    increment5img.place(x=1270,y=825)
    increment5txt=Label(master=mpWindow,text="Forward",justify='center',font=("Helvetica"))
    increment5txt.place(x=1270,y=930,width=107)  
     
    forward_image_take = ImageTk.PhotoImage(Image.open('Pictures/forward.png').resize((100,100)))
    forward_btn_img = Button(mpWindow,image=forward_image_take,bg="#323232", activebackground="#323232", relief=RAISED,bd=3)
    forward_btn_img.place(x=1450,y=825)
    forwardbtntxt=Label(master=mpWindow,text="Next Song",justify='center',font=("Helvetica"))
    forwardbtntxt.place(x=1450,y=930,width=107)   

    volumeup = ImageTk.PhotoImage(Image.open('Pictures/volumeup.png').resize((100,100)))
    volumeupimg = Button(mpWindow,image=volumeup,bg="#323232", activebackground="#323232", relief=RAISED,bd=3,command=volumeupfun)
    volumeupimg.place(x=1630,y=825)
    volumeuptxt=Label(master=mpWindow,text="Volume Up",justify='center',font=("Helvetica"))
    volumeuptxt.place(x=1630,y=930,width=107)  
    
    def slide(x):
        # Tinfly.pause_song()
        Tinfly.slideplaysong()
    
    slider=ttk.Scale(mpWindow,from_=0,to=100,orient=HORIZONTAL,value=0,command=slide,length=700)
    slider.place(x=640,y=600)
    
    Tinfly=MusicPlayer(mpWindow,backward_btn_img,play_btn_img,pause_btn_img,stop_btn_img,forward_btn_img)
    MusicPlay.protocol("WM_DELETE_WINDOW", closewindow)
    MusicPlay.mainloop()


def lWindow():
    
    
    def dbconnect():
        import mysql.connector
        try:
            global mydb
            mydb=mysql.connector.connect(host="localhost",user="root",password="",database="tinfly")
            print("Connection Successful !")
            tts("Database Connection Successful !")
        except:
            print("Connection Error !")
            tts("Database Connection Error !")
            loginWindow.destroy()
            # sys.exit(0)
    
    dbconnect()
    
    def checklogin():   
        # dbconnect()
        user=usernameentry.get()
        pwd=passwordentry.get()
        q="select * from login"
        flag=True
        try:
            status=False
            cur=mydb.cursor()
            cur.execute(q)
            dbs=cur.fetchall()
            for x in dbs:
                if x[0]==user and x[1]==pwd:
                    status=True
                    break
            if status:
                print("Login Successful !")
                tts("Login Successful !")
                flag==True
            else:
                print("Invalid Login !")
                tts("Invalid Login !")
                flag=False
        except:
            print("Database Connection Error !")
            tts("Database Connection Error !")
        if flag:
            loginWindow.destroy()
            tts("Welcome "+user)
        else:
            sys.exit(0)
            
    global password
    password=[]  
              
    def regexsolver():
        import re

        count=0
        boolval=False
        for p in password:
            if len(p)>=5:
                dmo=re.search(r"\d",p)
                if dmo:
                    count+=1
                    cmo=re.search(r"[A-Z]+",p)
                    if cmo:
                        count+=1
                        scmo=re.search(r"\w+\W+",p)
                        if scmo:
                            count+=1
                        else:
                            print("No Special Symbols in Password")
                            tts("No Special Symbols in Password")
                    else:
                        print("No Capital letters in Password")
                        tts("No Capital letters in Password")
                else:
                    print("No Digits in Password")
                    tts("No Digits in Password")
            else:
                print("Password Length less than 5 character")
                tts("Password Length less than 5 character")
            # print(count)
            if count==3:
                boolval=True
            else:
                boolval=False
            return boolval
       
    def signup():
        user=usernameentry.get()
        pwd=passwordentry.get()
        password.append(pwd)
        if regexsolver()==True:
            password.pop()
            mycursor = mydb.cursor()

            sql = "INSERT INTO login (username, password) VALUES (%s, %s)"
            val = (user, pwd)
            mycursor.execute(sql, val)
            mydb.commit()
            tts("New User "+user+" added")
            loginWindow.destroy()
        else:
            print("Password not according to pattern")
            tts("Password not according to pattern")
        
    
    loginWindow=Toplevel(root)
    loginWindow.title("Login")
    loginWindow.state("zoomed")
    
    #images
    bgimg = Image.open("Photos/bg.jpg")
    resize_image = bgimg.resize((1920,1024))
    bgimg = ImageTk.PhotoImage(resize_image)

    loginimg= Image.open("Photos/login.jpg")
    resize_image = loginimg.resize((390,130))
    loginimg = ImageTk.PhotoImage(resize_image)

    signupimg= Image.open("Photos/signup.jpg")
    resize_image = signupimg.resize((390,130))
    signupimg = ImageTk.PhotoImage(resize_image)

    tinflyimg = Image.open("Photos/tinfly.png")
    resize_image = tinflyimg.resize((423,150))
    tinflyimg = ImageTk.PhotoImage(resize_image)
     
    loginframe = Frame(master=loginWindow,width=1680,height=1440)
    loginframe.pack()    
    
    loginbg = Label(master= loginframe, image = bgimg)
    loginbg.pack()
    
    tinflylabel = Label(master=loginframe,text="TinFly",image = tinflyimg)
    tinflylabel.place(x=727,y=50)
    
    usernametext=Label(master=loginframe,text="Enter Username",justify='center',font=("Helvetica"))
    usernametext.place(x=400,y=275,width=205)
    
    usernameentry = Entry(master=loginframe, background="#ffffff", font=("Helvetica", 32))
    usernameentry.place(x=800,y=250,width=790,height=75)
    
    passwordtext=Label(master=loginframe,text="Enter Password",justify='center',font=("Helvetica"))
    passwordtext.place(x=400,y=475,width=205)
    
    passwordentry =Entry(master=loginframe, background="#ffffff", font=("Helvetica", 32),show="*")
    passwordentry.place(x=800,y=450,width=790,height=75)
    
    loginbtn = Button(master=loginframe,text="Login",command=checklogin,image=loginimg)
    loginbtn.place(x=350,y=650)
    
    signupbtn = Button(master=loginframe,text="Sign Up",command=signup,image=signupimg)
    signupbtn.place(x=1150,y=650)
    
    loginWindow.mainloop()



def whatsappWindow():
    
    def whatsappsend():
        phno=phnoentry.get()
        msg=msgentry.get("1.0", "end-1c")
        whatsappchecksend(phno,msg)
        
    wWindow=Toplevel(root)
    wWindow.title("Whatsapp")
    wWindow.state("zoomed")
    
    #images
    bgimg = Image.open("Photos/bg.jpg")
    resize_image = bgimg.resize((1920,1024))
    bgimg = ImageTk.PhotoImage(resize_image)

    tinflyimg = Image.open("Photos/tinfly.png")
    resize_image = tinflyimg.resize((423,150))
    tinflyimg = ImageTk.PhotoImage(resize_image)
    
    sendimg = Image.open("Photos/whatsappsend.png")
    resize_image = sendimg.resize((400,144))
    sendimg = ImageTk.PhotoImage(resize_image)
    
    whatsappframe = Frame(master=wWindow,width=1680,height=1440)
    whatsappframe.pack()    
    
    whatsappbg = Label(master= whatsappframe, image = bgimg)
    whatsappbg.pack()
    
    tinflylabel = Label(master=whatsappframe,text="TinFly",image = tinflyimg)
    tinflylabel.place(x=727,y=50)
    
    phnotext=Label(master=whatsappframe,text="Enter Phone Number",justify='center',font=("Helvetica"))
    phnotext.place(x=400,y=275,width=205)
    
    phnoentry = Entry(master=whatsappframe, background="#ffffff", font=("Helvetica", 32))
    phnoentry.place(x=800,y=250,width=790,height=75)
    
    msgtext=Label(master=whatsappframe,text="Enter Message",justify='center',font=("Helvetica"))
    msgtext.place(x=400,y=475,width=205)
    
    msgentry = Text(master=whatsappframe, background="#ffffff", font=("Helvetica", 32))
    msgentry.place(x=800,y=450,width=790,height=200)
    
    sendbtn = Button(master=whatsappframe,text="send",image = sendimg, command=whatsappsend)
    sendbtn.place(x=750,y=750)
    
    wWindow.mainloop()
    
#images
mic= Image.open("Photos/mic.png")
resize_image = mic.resize((70,70))
mic = ImageTk.PhotoImage(resize_image)

search= Image.open("Photos/search.png")
resize_image = search.resize((70,70))
search = ImageTk.PhotoImage(resize_image)

downloads= Image.open("Photos/downloads.png")
resize_image = downloads.resize((100,100))
downloads = ImageTk.PhotoImage(resize_image)

whatsapp= Image.open("Photos/whatsapp.png")
resize_image = whatsapp.resize((100,100))
whatsapp = ImageTk.PhotoImage(resize_image)

gestures= Image.open("Photos/gestures.png")
resize_image = gestures.resize((100,100))
gestures = ImageTk.PhotoImage(resize_image)

googleimg= Image.open("Photos/google.png")
resize_image = googleimg.resize((100,100))
googleimg = ImageTk.PhotoImage(resize_image)

infoimg= Image.open("Photos/information.png")
resize_image = infoimg.resize((100,100))
infoimg = ImageTk.PhotoImage(resize_image)

guiimg = Image.open("Photos/gui.jpg")
resize_image = guiimg.resize((1920,1024))
guiimg = ImageTk.PhotoImage(resize_image)

playlistimg = Image.open("Photos/playlist.png")
resize_image = playlistimg.resize((200,200))
playlistimg = ImageTk.PhotoImage(resize_image)

musicimg = Image.open("Photos/music.png")
resize_image = musicimg.resize((100,100))
musicimg = ImageTk.PhotoImage(resize_image)

profileimg = Image.open("Photos/profile_icon.png")
resize_image = profileimg.resize((100,100))
profileimg = ImageTk.PhotoImage(resize_image)

bookimg = Image.open("Photos/book.png")
resize_image = bookimg.resize((200,200))
bookimg = ImageTk.PhotoImage(resize_image)

paintimg = Image.open("Photos/paint.png")
resize_image = paintimg.resize((200,200))
paintimg = ImageTk.PhotoImage(resize_image)

frame = Frame(master=root,width=1680,height=1440)
frame.pack()

guilabel = Label(master= frame, image = guiimg)
guilabel.pack()

def drawerscreen():
    profilebtn = Button(master=frame,text="Profile",image =profileimg,command=lWindow)
    profilebtn.place(x=240,y=100)
    profiletxt=Label(master=frame,text="Profile",justify='center',font=("Helvetica"))
    profiletxt.place(x=240,y=200,width=104)
    
    musicbtn = Button(master=frame,text="Play Music",image = musicimg, command=musicfileopen)
    musicbtn.place(x=240,y=500)
    musictxt=Label(master=frame,text="Play Music",justify='center',font=("Helvetica"))
    musictxt.place(x=240,y=600,width=104)
    
    googlebtn = Button(master=frame,text="Google",image = googleimg, command=googlefun)
    googlebtn.place(x=60,y=300)
    googletxt=Label(master=frame,text="Google",justify='center',font=("Helvetica"))
    googletxt.place(x=60,y=400,width=105)
    
    infobtn = Button(master=frame,text="Information",image = infoimg, command=infofun)
    infobtn.place(x=420,y=300)
    infotxt=Label(master=frame,text="Information",justify='center',font=("Helvetica"))
    infotxt.place(x=420,y=400,width=105)
    
    gesturebtn = Button(master=frame,text="Enable Gestures",image = gestures, command=gesturesx)
    gesturebtn.place(x=40,y=800)
    gesturetxt=Label(master=frame,text="Gestures",justify='center',font=("Helvetica"))
    gesturetxt.place(x=40,y=900,width=105)
    
    downloadbtn = Button(master=frame,text="Download",image = downloads, command=downloadvideo)
    downloadbtn.place(x=240,y=800)
    downloadtxt=Label(master=frame,text="Download",justify='center',font=("Helvetica"))
    downloadtxt.place(x=240,y=900,width=105)

    whatsappbtn = Button(master=frame,text="Whatsapp",image = whatsapp, command=whatsappWindow)
    whatsappbtn.place(x=440,y=800)
    whatsapptxt=Label(master=frame,text="Whatsapp",justify='center',font=("Helvetica"))
    whatsapptxt.place(x=440,y=900,width=105)


#homescreen

query = Entry(master=frame, background="#ffffff", font=("Helvetica", 32))
query.place(x=800,y=250,width=790,height=75)
querytext=Label(master=frame,text="Search Bar",justify='center',font=("Helvetica"))
querytext.place(x=801,y=325,width=790)

searchbtn = Button(master=frame,text="Search",image = search, command=playvideox)
searchbtn.place(x=1610,y=250)
searchtext=Label(master=frame,text="Search",justify='center',font=("Helvetica"))
searchtext.place(x=1610,y=320,width=75)

audiobtn = Button(master=frame,text="Audio",image = mic, command=sttx)
audiobtn.place(x=1700,y=250)
audiotxt=Label(master=frame,text="Audio",justify='center',font=("Helvetica"))
audiotxt.place(x=1700,y=320,width=75)

playlistbtn = Button(master=frame,text="Playlist",image = playlistimg, command=musicPlayerWindow)
playlistbtn.place(x=800,y=450)
playlisttext=Label(master=frame,text="Create Playlist",justify='center',font=("Helvetica"))
playlisttext.place(x=800,y=650,width=205)

bookbtn = Button(master=frame,text="E-Book",image = bookimg, command=ebookreader)
bookbtn.place(x=1200,y=450)
booktext=Label(master=frame,text="Select E-Book",justify='center',font=("Helvetica"))
booktext.place(x=1200,y=650,width=205)

paintbtn = Button(master=frame,text="Paint",image = paintimg, command=voicedraw)
paintbtn.place(x=1600,y=450)
painttext=Label(master=frame,text="Voice Draw",justify='center',font=("Helvetica"))
painttext.place(x=1600,y=650,width=205)

drawerscreen()
tts("Welcome To Tinfly")
root.mainloop()