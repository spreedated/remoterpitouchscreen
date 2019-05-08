#!/usr/bin/python
import socket
import os
import datetime
from subprocess import Popen
from subprocess import PIPE
import sys
from pyautogui import press, typewrite, hotkey

UDP_IP_ADDRESS = '192.168.1.137'
UDP_PORT_NO = 15548
version = '0.1'

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
print('+ ------------------------- +\n| Server ' + str(version) + ' ready to work! |\n+ ------------------------- +\n\n')
print('Waiting for commuication from cliens on port ' + str(UDP_PORT_NO) + '...')

while True:
	data, addr = serverSock.recvfrom(1024)
	if(len(data) > 1):
		pass
	else:
		continue
	try:
		cmd = data.decode().split("#")
		#Data Work
		if 'key' in cmd[0]:
			press(cmd[1])
		if 'hotkey' in cmd[0]:
			hotkey(cmd[1],cmd[2])
		if 'typewrite' in cmd[0]:
			typewrite(cmd[1])
		if 'program' in cmd[0]:
			os.system(cmd[1])
		# p = Popen(['/src/raspberry-remote/send',socket[0],socket[1],socket[2]], stdout=PIPE, stderr=PIPE)
		# stdout, stderr = p.communicate()
		# stdout = stdout.replace('\n',' --- ')
		# stderr = stderr.replace('\n',' --- ')

		# if(len(stdout) <= 0):
		# 	print('Some other error')
		# else:
		# 	print('Should work fine')
	except Exception as e:
		print('Error:' + str(e))
	except KeyboardInterrupt:
		print('User has killed me ;(')
