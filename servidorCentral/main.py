import sys
from time import sleep
from menu import print_menu
from socketServidor import inicializaSocket
from threading import Thread


if __name__ == '__main__':
    port = int(sys.argv[1])

    socketCentral = Thread(target=inicializaSocket,args=(port,),daemon=True)
    socketCentral.start()
    sleep(1)
    print_menu()