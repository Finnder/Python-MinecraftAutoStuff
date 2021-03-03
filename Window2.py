import tkinter as tk
import time
import keyboard
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Listener
import pywinauto

#While Loop Running?
running = True

#Declared Variable for further use
activeText = "null"

def NewWindow():
    global activeText
    global window2

    #Init Window2
    window2 = tk.Tk()
    window2.geometry("600x350")
    window2.title("Minecraft Auto-Stuff Program | By: Finn")
    window2.resizable(False, False)
    window2.configure(bg="PaleGreen2")

    # TITLE
    title_window2 = tk.Label(text="AUTO Commands", font=("Terminal", 20), foreground="white", background="grey",width=40, height=2)

    # BUTTONS - Commands
    button_stripminer = tk.Button(text="STRIP MINER", font=("Terminal", 15), command=AUTO_Stripminer, width=40,height=2)
    button_clicker = tk.Button(text="CLICKER", font=("Terminal", 15), command=AUTO_Clicker, width=40, height=2)
    button_tbd1 = tk.Button(text="tbd", font=("Terminal", 15), width=40, height=2)
    button_tbd2 = tk.Button(text="tbd", font=("Terminal", 15), width=40, height=2)
    button_tbd3 = tk.Button(text="tbd", font=("Terminal", 15), width=40, height=2)

    #PACKER - Finalization For Graphics
    title_window2.pack(pady=3)
    button_stripminer.pack(padx=2, pady=2)
    button_clicker.pack(padx=2, pady=2)
    button_tbd1.pack(padx=2, pady=2)
    button_tbd2.pack(padx=2, pady=2)
    button_tbd3.pack(padx=2, pady=2)

def StartMinecraft():
    pywinauto.application.Application(backend="uia").start("")

def ChangeApplicationFocus():
    pass


def CurrentActiveWindow():

    # Remove Window 2
    window2.destroy()

    # Activate The "Active Window"
    activeWindow = tk.Tk()
    activeWindow.geometry("500x100")
    activeWindow.title("Minecraft Auto-Stuff Program | By: Finn")
    activeWindow.resizable(False, False)
    activeWindow.configure(bg="black")

    # Active Label - Tells User What Is Active
    active = tk.Label(text=activeText, font=("Terminal", 20), bg="black", anchor="center")

    if running:
        active['fg'] = 'green'
    else:
        active['fg'] = 'red'

    #Packer
    active.pack(padx=2, pady=2)

#Controller For Da Mouse :D
mouse = Controller()

def AUTO_Stripminer():
    global activeText
    if running:
        activeText = "Strip Miner - Active"
    else:
        activeText = "Strip Miner - Not Active"

    CurrentActiveWindow()

    # While Loop For Stripminer
    while running:
        time.sleep(3)
        keyboard.press(hotkey='w')
        mouse.press(button=Button.left)


def AUTO_Clicker():
    global activeText
    if running:
        activeText = "Auto Clicker - Active"
    else:
        activeText = "Auto Clicker - Not Active"

    CurrentActiveWindow()

    while running:
        time.sleep(1)
        mouse.click(button=Button.left)
