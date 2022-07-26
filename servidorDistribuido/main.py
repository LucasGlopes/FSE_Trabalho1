import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

semaforoPrincipal = [20, 16, 12]
semaforoAuxiliar = [1, 26, 21]

GPIO.setup(semaforoPrincipal, GPIO.OUT)
GPIO.setup(semaforoAuxiliar, GPIO.OUT)

QTD_ESTADOS = 6
estadoAtual = 0

def estado0():
        GPIO.output([semaforoPrincipal[2], semaforoAuxiliar[2]], GPIO.HIGH)
        GPIO.output([semaforoPrincipal[0],semaforoPrincipal[1], semaforoAuxiliar[0],semaforoAuxiliar[1]], GPIO.LOW)
        sleep(1)

def estado1():
        GPIO.output([semaforoPrincipal[0],semaforoAuxiliar[2]], GPIO.HIGH)
        GPIO.output([semaforoPrincipal[1],semaforoPrincipal[2], semaforoAuxiliar[0],semaforoAuxiliar[1]], GPIO.LOW)
        sleep(10)

def estado2():
        GPIO.output([semaforoPrincipal[1], semaforoAuxiliar[2]], GPIO.HIGH)
        GPIO.output([semaforoPrincipal[0],semaforoPrincipal[2], semaforoAuxiliar[0],semaforoAuxiliar[1]],GPIO.LOW)
        sleep(3)

def estado3():
        GPIO.output([semaforoPrincipal[2], semaforoAuxiliar[2]], GPIO.HIGH)
        GPIO.output([semaforoPrincipal[0],semaforoPrincipal[1], semaforoAuxiliar[0],semaforoAuxiliar[1]], GPIO.LOW)
        sleep(1)

def estado4():
        GPIO.output([semaforoPrincipal[2], semaforoAuxiliar[0]], GPIO.HIGH)
        GPIO.output([semaforoPrincipal[0],semaforoPrincipal[1], semaforoAuxiliar[1],semaforoAuxiliar[2]], GPIO.LOW)
        sleep(5)

def estado5():
        GPIO.output([semaforoPrincipal[2], semaforoAuxiliar[1]], GPIO.HIGH)
        GPIO.output([semaforoPrincipal[0],semaforoPrincipal[1], semaforoAuxiliar[0],semaforoAuxiliar[2]], GPIO.LOW)
        sleep(3)

estados = [estado0, estado1, estado2, estado3, estado4, estado5]



while True:
        estados[estadoAtual]()
        estadoAtual = (estadoAtual + 1) % QTD_ESTADOS

