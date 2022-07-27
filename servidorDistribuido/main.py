import RPi.GPIO as GPIO
from time import sleep
from gpioFunctions import apagaLeds, acendeLeds
# from values import CRUZAMENTO_1, CRUZAMENTO_2


semaforoPrincipal = [20, 16, 12]
semaforoAuxiliar = [1, 26, 21]

QTD_ESTADOS = 6
estadoAtual = 0
botaoPedestreAuxiliar = False

GPIO.setmode(GPIO.BCM)

GPIO.setup(semaforoPrincipal, GPIO.OUT)
GPIO.setup(semaforoAuxiliar, GPIO.OUT)

GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def trataBotao(channel):
        global botaoPedestreAuxiliar
        botaoPedestreAuxiliar = not botaoPedestreAuxiliar

GPIO.add_event_detect(8,GPIO.RISING,callback=trataBotao)

def atualizaEstado():
        global estadoAtual
        estadoAtual = (estadoAtual + 1) % QTD_ESTADOS

def estado0():
        acendeLeds([semaforoPrincipal[2], semaforoAuxiliar[2]])
        apagaLeds([semaforoPrincipal[0],semaforoPrincipal[1], semaforoAuxiliar[0],semaforoAuxiliar[1]])
        sleep(1)
        atualizaEstado()

def estado1():
        acendeLeds([semaforoPrincipal[0],semaforoAuxiliar[2]])
        apagaLeds([semaforoPrincipal[1],semaforoPrincipal[2], semaforoAuxiliar[0],semaforoAuxiliar[1]])
        sleep(20)
        atualizaEstado()

def estado2():
        acendeLeds([semaforoPrincipal[1], semaforoAuxiliar[2]])
        apagaLeds([semaforoPrincipal[0],semaforoPrincipal[2], semaforoAuxiliar[0],semaforoAuxiliar[1]])
        sleep(3)
        atualizaEstado()

def estado3():
        acendeLeds([semaforoPrincipal[2], semaforoAuxiliar[2]])
        apagaLeds([semaforoPrincipal[0],semaforoPrincipal[1], semaforoAuxiliar[0],semaforoAuxiliar[1]])
        sleep(1)
        atualizaEstado()

def estado4():
        acendeLeds([semaforoPrincipal[2], semaforoAuxiliar[0]])
        apagaLeds([semaforoPrincipal[0],semaforoPrincipal[1], semaforoAuxiliar[1],semaforoAuxiliar[2]])
        sleep(5)

        global estadoAtual
        global botaoPedestreAuxiliar
        max_time = 10
        curr_time = 5
        while curr_time < max_time and botaoPedestreAuxiliar == False:

                sleep(0.1)
                curr_time = curr_time + 0.1
        
        if botaoPedestreAuxiliar:
                estadoAtual = 0
                botaoPedestreAuxiliar = False
        else:
                atualizaEstado()

def estado5():
        acendeLeds([semaforoPrincipal[2], semaforoAuxiliar[1]])
        apagaLeds([semaforoPrincipal[0],semaforoPrincipal[1], semaforoAuxiliar[0],semaforoAuxiliar[2]])
        sleep(3)
        atualizaEstado()


estados = [estado0, estado1, estado2, estado3, estado4, estado5]



while True:
        estados[estadoAtual]()
        

