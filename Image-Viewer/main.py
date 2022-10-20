import tkinter as tk
from PIL import Image, ImageTk      # pip install pillow
from tkinter import filedialog
import os


win = tk.Tk()
win.title("Image Viewer")
win.geometry("1000x900")

images = []
current_img = 0


def open_folder():
    global win, images, current_img, img_label, prev_btn, next_btn

    if images != []:
        current_img = 0
        images.clear()

    path = filedialog.askdirectory(initialdir="C:/", title="Select a folder having images")
    print(path)

    if path == "":  # if user pressed cancel
        return

    for file in os.listdir(path):
        
        # if file is an image file
        if file[-3:] in ("png", "jpg", "bmp"):  
            img = Image.open(path + "/" + file)

            img_w, img_h = img.size

            if img_h > 800:
                img_h = 800
            if img_w > 900:
                img_w = 900
            
            img = img.resize((img_w, img_h))
            
            imgtk = ImageTk.PhotoImage(img)
            images.append(imgtk)

    if images == []:
        img_label.configure(text="No Images found!")
    else:
        img_label.configure(image=images[current_img])
        prev_btn.configure(state="active")
        next_btn.configure(state="active")

    win.update()

def previous_img():
    global win, current_img, images, img_label

    if current_img == 0:
        current_img = len(images) - 1
    else:
        current_img -= 1

    img_label.configure(image=images[current_img])
    win.update()

def next_img():
    global win, current_img, images, img_label

    if current_img == len(images) - 1:
        current_img = 0
    else:
        current_img += 1

    img_label.configure(image=images[current_img])
    win.update()


label = tk.Label(win, text="Image Viewer", font=(None, 24), bg="light blue", height=2)
label.pack(side="top", fill="x")

folder_btn = tk.Button(win, text="Select Folder", font=("Helvetica", 24, "bold"), relief="solid", command=open_folder)
folder_btn.pack(side="bottom", fill="x")

prev_btn = tk.Button(win, text="<", font=(None, 24, "bold"), relief="solid", state="disabled", command=previous_img)
prev_btn.pack(side="left", fill="y")

next_btn = tk.Button(win, text=">", font=(None, 24, "bold"), relief="solid", state="disabled", command=next_img)
next_btn.pack(side="right", fill="y")

img_label = tk.Label(win, text="Choose a folder to view image(s)", font=(None, 24, "bold"))
img_label.pack(side="top", fill="both", expand=True)

win.mainloop()