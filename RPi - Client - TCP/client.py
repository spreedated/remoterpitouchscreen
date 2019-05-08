#!/usr/bin/python
import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 50000))
s.sendall('Hello, world'.encode())
data = s.recv(1024)
s.close()
print('Received', repr(data))
