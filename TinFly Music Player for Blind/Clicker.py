import pyautogui as pagui
import time as time

def multiple_clicker(key1, key2):
    pagui.keyDown(key1)
    pagui.press(key2)
    pagui.keyUp(key1)

def clicker(key):
    pagui.keyDown(key)
    time.sleep(1)
    pagui.keyUp(key)

