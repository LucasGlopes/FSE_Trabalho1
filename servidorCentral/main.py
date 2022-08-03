from time import sleep
from menu import print_menu
from socketServidor import inicializaSocket
from threading import Thread


if __name__ == '__main__':
    socketCentral = Thread(target=inicializaSocket, daemon=True)
    socketCentral.start()
    sleep(1)
    print_menu()