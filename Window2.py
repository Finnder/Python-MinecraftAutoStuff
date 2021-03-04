import tkinter as tk
import time
import keyboard
import os
from pynput.mouse import Button, Controller
import pywinauto

# While Loop Running?
running = True

# Declared Variable for further use
activeText = "null"


def NewWindow():
    global activeText
    global window2
    global willJump

    # Init Window2
    window2 = tk.Tk()

    window2.geometry("600x600")
    window2.title("Minecraft Auto-Stuff Program | By: Finn")
    window2.resizable(False, False)

    icon = tk.PhotoImage(file="Photos/icon.png")
    window2.iconphoto(False, icon)

    # BACKGROUND
    background_Image = tk.PhotoImage(file="Photos/background_dirt.png")
    bg_label = tk.Label(window2, image=background_Image)
    bg_label.place(x=0, y=0)

    # TITLE
    title_window2 = tk.Label(text="AUTO Commands", font=("Terminal", 25), fg="white", bg="SeaGreen3", width=40, height=2)

    # AUTO Stripminer
    stripminer_Image = tk.PhotoImage(file="Photos/diamondPick.png")
    button_stripminer = tk.Button(text="STRIP MINER", font=("Terminal", 15), bg="gray75",command=AUTO_Stripminer, width=300, height=100, image=stripminer_Image, compound="right")

    # AUTO Clicker
    clicker_Image = tk.PhotoImage(file="Photos/pointer.png")
    button_clicker = tk.Button(text="CLICKER", font=("Terminal", 15), command=AUTO_Clicker, width=300, height=100, image=clicker_Image, compound="right")

    # AUTO Run
    runner_Image = tk.PhotoImage(file="Photos/runner.png")
    button_run = tk.Button(text="RUNNER (W.I.P)", font=("Terminal", 15), bg="gray75", command=AUTO_Run, width=300, height=100, image=runner_Image, compound="right")
    willJump = tk.IntVar()
    jumpCheck = tk.Checkbutton(text="Jump? (Character Jumps While Running)", font=("Terminal", 10), bg="gray65", variable=willJump)  # Checkbox

    #TBD's
    button_tbd2 = tk.Button(text="tbd", font=("Terminal", 15), width=40, height=2)
    button_tbd3 = tk.Button(text="tbd", font=("Terminal", 15), width=40, height=2)

    # PACKER - Finalization For Graphics
    title_window2.pack()
    button_stripminer.pack(padx=2, pady=3)
    button_clicker.pack(padx=2, pady=3)
    button_run.pack(padx=2, pady=3)
    jumpCheck.pack(padx=1, pady=1)

    window2.mainloop()


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

    # Packer
    active.pack(padx=2, pady=2)


# Controller For Da Mouse :D
mouse = Controller()


# AUTO COMMANDS
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
        keyboard.press('w')
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
        mouse.click(Button.left, 1)


def AUTO_Run():
    global activeText
    if running:
        activeText = "Auto Run - Active"
    else:
        activeText = "Auto Run - Not Active"

    CurrentActiveWindow()

    if willJump.get() == 1:
        time.sleep(1)
        keyboard.press('w')

        while running:
            time.sleep(1)
            keyboard.press('space')
    else:
        time.sleep(2)
        keyboard.press('w')
        keyboard.release('w')
        keyboard.press('w')