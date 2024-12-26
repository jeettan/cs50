from tkinter import *
import time
import pygame
from pygame import mixer
import json
import atexit

root = Tk()
root.title("Lymphedema App")

root.resizable(0, 0)
root.geometry("400x300")

timer_running = False
break_counter = False
minute = 15
second = 0
wraps_completed = 0 
SPEED = 1000

logo = PhotoImage(file="logo.png")
root.iconphoto(False, logo)

mixer.init()

def pause():

    global timer_running

    timer_running = False

    status_lbl.config(text="**pause**", fg="red")

def resetAll():

    global wraps_completed

    wraps_completed = 0
    wraps_lbl.config(text=wraps_completed)
    status_lbl.config(text="**pause**", fg="black")
    reset()

def lookupWraps():

    global wraps_completed

    f = open('data.json')

    data = json.load(f)
    wraps_completed = data[0]['wraps_completed']

    f.close()

def saveWraps():

    global wraps_completed

    with open('data.json', 'r') as file:
        data = json.load(file)

        data[0]['wraps_completed'] = wraps_completed

    file.close()

    with open('data.json', 'w') as file:
        json.dump(data,file)

    file.close()

def start(self=None):

    global timer_running, break_counter

    if(timer_running==True):
        return

    timer_running = True
    status_lbl.config(text="**Running**", fg="black")

    if(break_counter==True):
        status_lbl.config(text="**break**", fg="black")

    timer()

def timer():
    global timer_running, minute, second, break_counter, wraps_completed, SPEED

    if(timer_running==False):
        return

    if(second==0 and minute==0 and break_counter==False):
        mixer.music.load('alarm.mp3')
        mixer.music.play()
        break_timer()
        wraps_completed = wraps_completed + 1
        wraps_lbl.config(text=wraps_completed)
        timer_running = False
        return

    if(second==0 and minute==0 and break_counter==True):
        reset()
        mixer.music.load('alarm.mp3')
        mixer.music.play()
        break_counter = False
        timer_running = False
        return

    if(second==0):
        second = 60
        minute = minute - 1
        minute_var.set(str(minute).zfill(2))

    second = second-1
    second_var.set(str(second).zfill(2)) 
    root.after(SPEED, timer)

def reset():
    global timer_running, minute, second, break_counter

    break_counter = False

    second = 0
    minute = 15
    timer_running = False

    second_var.set(str("00"))
    minute_var.set(str("15"))

    status_lbl.config(text="**pause**")

def break_timer():
    global minute, second, break_counter

    break_counter = True

    minute = 5
    second = 0

    status_lbl.config(text="**break**")
    minute_var.set(str(minute).zfill(2))
    second_var.set(str("00"))

minute_var = StringVar(value = '15 ')
second_var = StringVar(value = '00 ')

minute_lbl = Label(font=('Helvetica', 80), textvariable= minute_var)
colon_lbl = Label(font=('Helvetica', 80), text=":")
second_lbl = Label(font=('Helvetica', 80), textvariable= second_var)

counter_lbl = Label(font=('Helvetica', 18), text="Wraps completed: ")
counter_lbl.grid(column=0,row=0,padx=(10,0), pady=20)

lookupWraps()

wraps_lbl = Label(font=('Helvetica', 18), text=wraps_completed)
wraps_lbl.grid(column=1,row=0)

minute_lbl.grid(column=0, row=1, padx=(30,0))
colon_lbl.grid(column=1, row=1)
second_lbl.grid(column=2, row=1)

start_button = Button(text="Start", command=start)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset timer", command=reset)
reset_button.grid(column=1, row=2)

reset_button3 = Button(text="Reset all", command=resetAll)
reset_button3.grid(column=2, row=2)

status_lbl = Label(font=('Helvetica Bold', 18), text="**PAUSE**")
status_lbl.grid(column=0,row=3,pady=30)

pause_lbl = Button(text="pause", command=pause)
pause_lbl.grid(column=1,row=3,pady=30)

atexit.register(saveWraps)

root.mainloop()