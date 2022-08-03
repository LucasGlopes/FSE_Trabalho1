import socket
from _thread import *
from threading import Thread
from menu import atualizaInfo, cruzamentos
import json


connections = []

def thread_cliente(c):
    while True:
        data = c.recv(1024)
        if not data:
            # print('bye')
            break
        else:
            # c.send(data)
            # atualizaInfo(data)
            # json.loads(data)
            # cruzamentos.append(json.loads(data))
            atualizaInfo(json.loads(data))
    
    c.close()

def inicializaSocket():
    global connections
    host = "0.0.0.0"

    port = 10282
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    print("socket binded to port", port)

    s.listen(5)
    print("socket is listening")

    while True:
        c, addr = s.accept()
        connections.append(c)
        threadSocket = Thread(target=thread_cliente, args=(c,))
        threadSocket.start()

    s.close()

# if __name__ == '__main__':
# 	inicializaSocket()
