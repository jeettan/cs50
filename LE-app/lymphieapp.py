from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import customtkinter
import subprocess
import webbrowser

root = Tk()
root.title("Lymphedema App")

img = PhotoImage(file="background-le.png")
img2 = ImageTk.PhotoImage(Image.open("pic05.jpeg"))

logo = PhotoImage(file="logo.png")
root.iconphoto(False, logo)

root.resizable(False, False)

root.geometry("400x500")

canvas = Canvas(root, width=400, height=500)
canvas.place(x=0,y=0)
canvas.create_image(0, 0, image=img, anchor="nw")

def open_timer():
    subprocess.Popen(['python', 'timer.py'])

def open_data():
    subprocess.Popen(['python', 'LE-data.py'])

def website_link():
    webbrowser.open("https://www.lymphedema-thailand.com/")

label = Label(root, image = img2, highlightthickness=0, borderwidth=0)
label.grid(column=0, row=0, pady=(40,0))

title_text = Label(root, text="Lymphedema Management App", font=('Helvetica Bold', 22), bg="black", fg="white", height=1)
title_text.grid(column=0, row=1, pady=(50,0), padx=30)

button = customtkinter.CTkButton(root, text="Timer",fg_color="red", hover_color="maroon", command=open_timer)
button.grid(column=0,row=2, pady=(12,7))

button2 = customtkinter.CTkButton(root, text="Data/Results", border_width=0, command=open_data)
button2.grid(column=0,row=3, pady=7)

button3 = customtkinter.CTkButton(root, text="Information", fg_color="green", hover_color="green4", border_width=0, command=website_link)
button3.grid(column=0,row=4, pady=7)

root.mainloop()