from gpioFunctions import apagaLeds, acendeLeds
from time import sleep
from valores import TEMPO


def estado0(semaforoPrincipal, semaforoAuxiliar):
        acendeLeds([semaforoPrincipal[2], semaforoAuxiliar[2]])
        apagaLeds([semaforoPrincipal[0],semaforoPrincipal[1], semaforoAuxiliar[0],semaforoAuxiliar[1]])
        sleep(TEMPO['VERMELHO_TOTAL'])

def estado1(semaforoPrincipal, semaforoAuxiliar):
        acendeLeds([semaforoPrincipal[0],semaforoAuxiliar[2]])
        apagaLeds([semaforoPrincipal[1],semaforoPrincipal[2], semaforoAuxiliar[0],semaforoAuxiliar[1]])
        sleep(TEMPO['PRINCIPAL_VERDE_MINIMO'])

def estado2(semaforoPrincipal, semaforoAuxiliar):
        acendeLeds([semaforoPrincipal[1], semaforoAuxiliar[2]])
        apagaLeds([semaforoPrincipal[0],semaforoPrincipal[2], semaforoAuxiliar[0],semaforoAuxiliar[1]])
        sleep(TEMPO['AMARELO'])

def estado4(semaforoPrincipal, semaforoAuxiliar):
        acendeLeds([semaforoPrincipal[2], semaforoAuxiliar[0]])
        apagaLeds([semaforoPrincipal[0],semaforoPrincipal[1], semaforoAuxiliar[1],semaforoAuxiliar[2]])
        sleep(TEMPO['AUXILIAR_VERDE_MINIMO'])

def estado5(semaforoPrincipal, semaforoAuxiliar):
        acendeLeds([semaforoPrincipal[2], semaforoAuxiliar[1]])
        apagaLeds([semaforoPrincipal[0],semaforoPrincipal[1], semaforoAuxiliar[0],semaforoAuxiliar[2]])
        sleep(TEMPO['AMARELO'])


estados = [estado0, estado1, estado2, estado0, estado4, estado5]