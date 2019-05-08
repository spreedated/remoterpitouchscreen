#!/usr/bin/python
import tkinter as tk, threading
from tkinter import *
from PIL import ImageTk,Image
from tkinter import font
from functools import partial
import os
import imageio

#Global Vars
bgcolor = '#000000'
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
screen_width = 800
screen_height = 480
mypath = os.getcwd() + '/'

class Content:
	def __init__(self, master):
		#CONTENT - Main
		self.content_img = Image.open(mypath + 'img/content_main.png')
		self.content_img_r = ImageTk.PhotoImage(self.content_img)
		self.content_label = tk.Label(master, width=self.content_img_r.width(), height=self.content_img_r.height(), bd=0, highlightthickness=0, relief='flat', background='#000000', takefocus=0, image=self.content_img_r)
		self.content_label.pack()
		self.content_label.place(x=107, y=63)

# #Background -- resize to screen
# bg_img = Image.open(mypath + 'img/bg.png')
# bg_img =  bg_img.resize((screen_width,screen_height), Image.ANTIALIAS)
# bg_img_r = ImageTk.PhotoImage(bg_img)
# background_label = tk.Canvas(master, width=screen_width, height=screen_height, background=bgcolor, highlightthickness=0, bd=0)
# background_label.pack()
# background_label.create_image((bg_img_r.width()/2), (bg_img_r.height()/2), image=bg_img_r)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)


class Button:
	def __init__(self, master, image, x ,y):
		self.img = Image.open(image)
		self.img0 = ImageTk.PhotoImage(self.img)
		button1 = tk.Button(master, width=self.img0.width(), height=self.img0.height(), image=self.img0, bg=bgcolor, borderwidth=0, relief='flat', highlightthickness=0, activebackground=bgcolor)
		button1.pack()
		button1.place(x=x,y=y)

	def button1_click(stuff):
		bg_img2 = Image.open(mypath + 'img/button_configure.png')
		bg_img_2 = ImageTk.PhotoImage(bg_img2)
		stuff.configure(image=bg_img_2)
		stuff.image = bg_img_2
		print('button clicked')

#


if __name__ == "__main__":
	root = tk.Tk()
	#Root Window Fullscreen without bars (real fullscreen)
	#Root Window Configures
	# root.overrideredirect(True)
	# root.overrideredirect(False)
	# root.attributes('-fullscreen',True)
	root.geometry(str(screen_width) + 'x' + str(screen_height))
	#root.configure(background=bgcolor, cursor='none')
	mainwindow = Content(root)
	btn_config = Button(root, mypath + 'img/button_configure.png',11,383)

	root.mainloop()
