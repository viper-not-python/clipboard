from tkinter import Tk
from pynput import keyboard


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


def copy():
    ct = Tk().clipboard_get()
    with open("//fritz.nas/FRITZ.NAS/HDD/Share/AMG/cb.txt", "w") as ncb:
        ncb.write(ct)
    print(ct)
def paste():
    with open("//fritz.nas/FRITZ.NAS/HDD/Share/AMG/cb.txt", "r") as ncb:
        ct = ncb.read()
    Tk().clipboard_append(ct)
    print(ct)
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
            cpp = True
            execute("cp")

    if any([key in VOMBO for VOMBO in vp]):
        current.add(key)
        if any(all(j in current for j in VOMBO) for VOMBO in vp):
            print("v")
            vpp = True
            execute("vp")

def on_release(key):
    if any([key in COMBO for COMBO in ap]):
        current.remove(key)


#main


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

