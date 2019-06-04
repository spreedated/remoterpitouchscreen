#!/usr/bin/python
import socket
import os
import datetime
from subprocess import Popen
from subprocess import PIPE
import sys
from pywinauto import application
from pywinauto import keyboard
from pywinauto import mouse
import win32api
#from infi.systray import SysTrayIcon #Seems broken/not reliable on Windows
import select

UDP_IP_ADDRESS = '192.168.1.137'
UDP_PORT_NO = 15548
version = '0.4'

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
serverSock.setblocking(0)
print('+ ------------------------- +\n| Server ' + str(version) + ' ready to work! |\n+ ------------------------- +\n\n')
print('Waiting for commuication from clients on port ' + str(UDP_PORT_NO) + '...')

def ProcessCommand(cmd):
	if 'key' in cmd[0]:
		#Advanced, search for specific window and sendkeys, seems broken due to mouse cursor repositioning on no reason
		mousex, mousey = win32api.GetCursorPos() #Workaround for the broken mousecursor repositioning
		# (?i) <-- case-insensitive, regex
		# searchregex_string='(?i).*untitled.*atOm' # using ATOM editor, for debug purpose
		searchregex_string='(?i).*notepad*' #using NOTEPAD editor, for debug purpose
		#searchregex_string='(?i).*elite*client*' #main ED window on Windows
		app = application.Application().connect(title_re=searchregex_string)
		window = app.window(title_re=searchregex_string) #Second time the same title_re - is that correct?!
		window.type_keys(cmd[1])
		mouse.move(coords=(mousex, mousey)) #Workaround for the broken mousecursor repositioning

		#Simple, just sends keys to any window currently in focus
		#keyboard.send_keys(cmd[1])
		
		#Finally give some output
		print('Executed: ' + str(cmd[1]))
	if 'hotkey' in cmd[0]:
		hotkey(cmd[1],cmd[2])
	if 'typewrite' in cmd[0]:
		app = application.Application().connect(title_re='(?i).*elite*client')
		#app.UntitledNotepad.minimize()
		app.set_text(cmd[1])
	if 'program' in cmd[0]:
		os.system(cmd[1])

#systray = SysTrayIcon("ico/icon.ico", "Remote RPi Server", on_quit=Exit, default_menu_index=0)
if __name__ == '__main__':
	#systray.start()
	try:
		while True:
			ready = select.select([serverSock], [], [], 5) # Using SELECT (timeout 5 seconds) to not block the while loop (preventing console blockade [CTRL+C])
			if ready[0]: #Go ahead if there's actual DATA/Package
				data, addr = serverSock.recvfrom(1024) #Wait for DATA/Package
				try:
					cmd = data.decode().split("#")
					#Data Work
					ProcessCommand(cmd)
				except Exception as e:
					print('Error:' + str(e))
	except KeyboardInterrupt:
				print('Good Bye!')
