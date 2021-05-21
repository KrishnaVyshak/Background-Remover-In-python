import tkinter as tk
from tkinter import W

import requests
from tkinter.ttk import *
# Top level window
frame = tk.Tk()
frame.title("Background Remover - by Krishnavyshak")
frame.geometry('400x200')
frame.iconbitmap('icon.ico')
# Function for getting Input
# from textbox and printing it
# at label widget
title = tk.Label(frame, text="Background Eraser", font=("Helvetica", 25))
credit = tk.Label(frame, text="Created By Krishnavyshak", font=("Helvetica", 9))

title.pack()
credit.pack()
def printInput():
    path = inputtxt.get(1.0, "end-1c")

    response = requests.post(
        'https://api.remove.bg/v1.0/removebg?',
        files={'image_file': open(path, 'rb')},
        data={'size': 'auto', 'bg_color': '#ffffff'},
        headers={'X-Api-Key': 'MF8X99DWyaPjzLRx5qXNpFqN'},
    )

    image_name = inputtxt2.get(1.0, "end-1c")
    if response.status_code == requests.codes.ok:
        with open(image_name + '.png', 'wb') as out:
            out.write(response.content)
        lbl.config(text="Background Erased Successfully!")
    else:
        print("Error:", response.status_code, response.text)



tag1 = tk.LabelFrame(frame, text="Enter Image Path")
inputtxt = tk.Text(tag1,
				height = 1,
				width = 20)

tag1.pack()
inputtxt.pack()

tag2 = tk.LabelFrame(frame, text="Enter Image Name")
inputtxt2 = tk.Text(tag2,
				height = 1,
				width = 20)
png = tk.Label(tag2, text=".png")
tag2.pack()
inputtxt2.pack()

# Button Creation
printButton = tk.Button(frame,
						text = "Erase Background",
						command = printInput,
                        width=22)
printButton.pack()

# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()
