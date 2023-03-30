import socket 
from threading import Thread
from tkinter import *

#nickname = input("Choose your nickname: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))

(def receive():
while True:
conn, addr = server.accept()
conn. send('NICKNAME'.encode('utf-8'))
nickname = conn.recv(2048).decode('utf-8')
list_of_clients.append(conn) 
nicknames.append(nickname) 
print (nickname + " connected!")
new_thread = Thread(target= clientthread, args=(conn, nickname))
new_thread.start()) 

def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('utf-8'))

receive_thread = Thread(target=receive)
receive_thread.start()
write_thread = Thread(target=write)
write_thread.start()