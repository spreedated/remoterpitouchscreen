#!/usr/bin/python
import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 50000))
s.listen(1)
conn, addr = s.accept()

while 1:
	data = conn.recv(1024)
	print(data[0])
	# if not data:
	# 	break
	#conn.sendall(data)
conn.close()
