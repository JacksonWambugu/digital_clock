import sys
from tkinter import *
import time

def times():
    current_time = time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(200,times)
    
root=Tk()
root.geometry("500x250")
clock=Label(root,font=("times",60,"bold"),bg="cyan")
clock.grid(row=2,column=2,padx=100,pady=25)
times()
digi=Label(root,text="Digital Clock",font="times 24 bold")
digi.grid(row=0,column=2)
nota=Label(root,text="Hours  Minutes Seconds  ",font="times  15 bold")
nota.grid(row=3,column=2)
root.mainloop()
