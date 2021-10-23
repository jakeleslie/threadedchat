import socket, threading, os, math, sys

TCP_IP = '127.0.0.1'

TCP_PORT = 5005

BUFFER_SIZE = 1024

#af_inet is IPV4, sock stream is tcp. streaming socket!
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

while True:
    msg = s.recv(BUFFER_SIZE)

    print(msg.decode("utf-8"))