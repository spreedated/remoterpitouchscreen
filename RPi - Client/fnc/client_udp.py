#!/usr/bin/python
import socket
import sys
import datetime

if len(sys.argv) >= 2:
	Message = sys.argv[1] + "#" + sys.argv[2]
else:
	print("Not enough arguments!")
	sys.exit()

now = datetime.datetime.now()
rightnow = '[ '+str(now.day)+'.'+str(now.month)+'.'+str(now.year)+' -- '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)+':'+str(now.microsecond)+' ] '

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
	UDP_IP_ADDRESS = '192.168.1.137'
	UDP_PORT_NO = 15548
	clientSock.sendto(Message.encode(), (UDP_IP_ADDRESS, UDP_PORT_NO))

	print(rightnow + 'sent to ' + UDP_IP_ADDRESS + ':' + str(UDP_PORT_NO))
except Exception as e:
	print("Error: " + rightnow + str(e))
