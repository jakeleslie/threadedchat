import socket, threading, os, math, sys

TCP_IP = '127.0.0.1'

TCP_PORT = 5005

BUFFER_SIZE = 1024

#af_inet is IPV4, sock stream is tcp. streaming socket!
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))

s.listen(1)

#listen forever for a connection
while 1:
    conn, addr = s.accept() #if anybody connects we accept it 
    print('Connection address: ', addr)
    conn.send(bytes("Welcome to the server!", "utf-8"))
    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        print("Received data: ", data)
        conn.send(data) 
        conn.close()
