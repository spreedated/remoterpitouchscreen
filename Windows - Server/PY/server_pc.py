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
#from infi.systray import SysTrayIcon
import atexit

UDP_IP_ADDRESS = '192.168.1.137'
UDP_PORT_NO = 15548
version = '0.3'

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
print('+ ------------------------- +\n| Server ' + str(version) + ' ready to work! |\n+ ------------------------- +\n\n')
print('Waiting for commuication from clients on port ' + str(UDP_PORT_NO) + '...')

def ProcessCommand(cmd):
	if 'key' in cmd[0]:
		#mousex, mousey = win32api.GetCursorPos()

		#app = application.Application().connect(title_re='(?i).*untitled.*atOm')
		#Form1 = app.window(title_re='(?i).*untitled.*atOm')
		#Form1.type_keys('dasdas ' + cmd[1])

		#mouse.move(coords=(mousex, mousey))

		keyboard.send_keys(cmd[1])
		print('Executed: ' + str(cmd[1]))
	if 'hotkey' in cmd[0]:
		hotkey(cmd[1],cmd[2])
	if 'typewrite' in cmd[0]:
		app = application.Application().connect(title_re='(?i).*notepad$')
		#app.UntitledNotepad.minimize()
		app.set_text(cmd[1])
	if 'program' in cmd[0]:
		os.system(cmd[1])

do_quit = False

def Exit(self):
    do_quit = True

#systray = SysTrayIcon("ico/icon.ico", "Remote RPi Server", on_quit=Exit, default_menu_index=0)
if __name__ == '__main__':
	#systray.start()
	try:
		while do_quit == False:
			data, addr = serverSock.recvfrom(1024)
			if(len(data) > 1):
				pass
			try:
				cmd = data.decode().split("#")
				#Data Work
				ProcessCommand(cmd)
			except Exception as e:
				print('Error:' + str(e))
	except KeyboardInterrupt:
				print('User has killed me ;(')

def AtExit():
	print('Good Bye!')

atexit.register(AtExit)