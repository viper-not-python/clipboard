from tkinter import Tk
from pynput import keyboard
import time
import os
import sys
import pyperclip

#setup


cp = [
    {keyboard.Key.alt_l, keyboard.Key.shift, keyboard.KeyCode(char='c')},
    {keyboard.Key.alt_l, keyboard.Key.shift, keyboard.KeyCode(char='C')}
]

vp = [
    {keyboard.Key.alt_l, keyboard.Key.shift, keyboard.KeyCode(char='v')},
    {keyboard.Key.alt_l, keyboard.Key.shift, keyboard.KeyCode(char='V')}
]

ap = [
    {keyboard.Key.alt_l, keyboard.Key.shift, keyboard.KeyCode(char='v'), keyboard.KeyCode(char='c')},
    {keyboard.Key.alt_l, keyboard.Key.shift, keyboard.KeyCode(char='V'), keyboard.KeyCode(char='c')},
    {keyboard.Key.alt_l, keyboard.Key.shift, keyboard.KeyCode(char='v'), keyboard.KeyCode(char='C')},
    {keyboard.Key.alt_l, keyboard.Key.shift, keyboard.KeyCode(char='V'), keyboard.KeyCode(char='C')}
]

current = set()


#defs

def get_cb():
    return Tk().clipboard_get()

def copy():
    with open("//fritz.nas/FRITZ.NAS/HDD/Share/AMG/cb.txt", "w") as ncb:
        ncb.write(get_cb())
    print(get_cb())

def paste():
    with open("//fritz.nas/FRITZ.NAS/HDD/Share/AMG/cb.txt", "r") as ncb:
        nct = ncb.read()

    pyperclip.copy(nct)
    pyperclip.paste()

    print(nct)

def execute(wk):
    if wk == "cp":
        copy()
    if wk == "vp":
        paste()

def on_press(key):
    if any([key in COMBO for COMBO in cp]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in cp):
            print("c")
            execute("cp")

    if any([key in VOMBO for VOMBO in vp]):
        current.add(key)
        if any(all(j in current for j in VOMBO) for VOMBO in vp):
            print("v")
            execute("vp")

def on_release(key):
    if any([key in COMBO for COMBO in ap]):
        current.remove(key)


#main


try:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
except:
    with open("//fritz.nas/FRITZ.NAS/HDD/Share/AMG/fails.log", "a") as log:
        log.write("failed at " + str(time.strftime('%X %x %Z')))
        os.execl(sys.executable, sys.executable, *sys.argv)