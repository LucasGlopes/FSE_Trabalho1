import socket
from _thread import *
from threading import Thread
from menu import atualizaInfo
import json
import pickle


conexoes = []

def thread_cliente(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        else:
            atualizaInfo(pickle.loads(data))
    
    c.close()

def inicializaSocket(port):
    global conexoes
    host = "0.0.0.0"
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    print("socket binded to port", port)

    s.listen(5)
    print("socket is listening")

    while True:
        c, addr = s.accept()
        conexoes.append(c)
        threadSocket = Thread(target=thread_cliente, args=(c,))
        threadSocket.start()


