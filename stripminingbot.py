import tkinter as tk

#WINDOWS
from Window2 import NewWindow

password = "1234Finn"
running = True

#FUNCTIONS
def confirmButtonCommand():
    userInput = passwordEntry.get()
    if userInput == password:
        print("LOG: " + "Button Worked")
        window.destroy()
        NewWindow()


# TKINTER STARTING WINDOW (Front-End)
window = tk.Tk()
window.geometry("600x300")
window.title("Minecraft Auto-Stuff Program | By: Finn")
window.resizable(False, False)

title = tk.Label(text="Minecraft Auto-stuff Program", font=("Terminal", 20),foreground="white", background="grey", width=30, height=2)
greeting = tk.Label(text="Hello, Please Enter The Password", font=("Terminal", 15), foreground="white", background="black", width=25, height=2)

passwordEntry = tk.Entry(fg="blue", bg="grey", show="*", justify="center",font=("Terminal", 20), width=20)
confirmButton = tk.Button(text="CONFIRM", font=("Terminal", 15), fg="yellow", bg="black", height=8, command=confirmButtonCommand)



# TKINTER (PACKER)
title.pack(padx=5, pady=5, fill=tk.BOTH)
greeting.pack(padx=5, pady=5, fill=tk.BOTH)
passwordEntry.pack(padx=5, pady=5, fill=tk.BOTH)
confirmButton.pack(padx=5, pady=5, fill=tk.BOTH)
window.mainloop()



