import keyboard
import time
import os
import sys
import pyperclip


#defs
def copy():
    with open("//fritz.nas/FRITZ.NAS/HDD/Share/AMG/cb.txt", "w") as ncb:
        ncb.write(pyperclip.paste())
    print(pyperclip.paste())

def paste():
    with open("//fritz.nas/FRITZ.NAS/HDD/Share/AMG/cb.txt", "r") as ncb:
        nct = ncb.read()
    print(nct)
    pyperclip.paste()
    pyperclip.copy(nct)

def execute(wk):
    if wk == "cp":
        copy()
    if wk == "vp":
        paste()


#main
while True:
    try:
        keyboard.wait("shift")
        while (keyboard.is_pressed("shift")):
            if keyboard.is_pressed("alt"):
                if keyboard.is_pressed("c"):
                    copy()
                    print("c")
                    while (keyboard.is_pressed("c")):
                        pass
                if keyboard.is_pressed("v"):
                    paste()
                    print("v")
                    while (keyboard.is_pressed("v")):
                        pass
    except:
        with open("//fritz.nas/FRITZ.NAS/HDD/Share/AMG/fails.log", "a") as log:
            log.write("failed at " + str(time.strftime('%X %x %Z')) + "\n")
            #os.execl(sys.executable, sys.executable, *sys.argv)