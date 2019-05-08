#!/usr/bin/python
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
from tkinter import font
import os

root = tk.Tk()

#Global Vars
bgcolor = '#000000'
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#Root Window Fullscreen without bars (real fullscreen)
#Root Window Configures
root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen',True)
root.geometry(str(screen_width) + 'x' + str(screen_height))
root.configure(background=bgcolor, cursor='none')

#Background -- resize to screen
bg_img = Image.open('img/bg.png')
bg_img =  bg_img.resize((screen_width,screen_height), Image.ANTIALIAS)
bg_img_r = ImageTk.PhotoImage(bg_img)
background_label = tk.Label(root, image=bg_img_r, width=screen_width, height=screen_height, background=bgcolor, highlightthickness=0, bd=0)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# #Logo Image
# img = ImageTk.PhotoImage(file='logo_transparent_black_500.png')
# frame0 = tk.Frame(root, bg=bgcolor)
# frame0.pack()
# frame0.place(x=((screen_width/2)-(img.width()/2)),y=10)
# canvas = Canvas(frame0, bg=bgcolor, width = img.width(), height = img.height(), highlightthickness=0)
# canvas.pack()
# canvas.create_image((img.width() / 2), 77, image=img)

# class Button:
# 	def __init__(self, master):

#Button with Image
frame1 = tk.Frame(root, bg=bgcolor)
frame1.pack()
frame1.place(x=43,y=144)

def button1_click():
	os.system(os.getcwd() + '/client_rpi.py key a')

img0 = ImageTk.PhotoImage(file='img/left_button.png')
button1 = tk.Button(frame1, width=184, height=55, image=img0, bg=bgcolor, borderwidth=0, command=lambda : button1_click())
button1.pack()
helv36 = font.Font(family="Consolas",size=12,weight="bold")
button1_label = tk.Label(button1, highlightthickness=0, bd=0, text='<<', bg='black', foreground='#AA0000', font=helv36)
button1_label.place(x=80, y=15)

#Button with Image
frame2 = tk.Frame(root, bg=bgcolor)
frame2.pack()
frame2.place(x=570,y=144)

def button2_click():
	os.system(os.getcwd() + '/client_rpi.py key d')

img1 = ImageTk.PhotoImage(file='img/right_button.png')
button2 = tk.Button(frame2, width=184, height=55, image=img1, bg=bgcolor, borderwidth=0, command=lambda : button2_click())
button2.pack()
helv36 = font.Font(family="Consolas",size=12,weight="bold")
button2_label = tk.Label(button2, highlightthickness=0, bd=0, text='>>', bg='black', foreground='#AA0000', font=helv36)
button2_label.bind(lambda : button2_click())
button2_label.place(x=80, y=15)


root.mainloop()
