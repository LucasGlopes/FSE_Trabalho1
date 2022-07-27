import RPi.GPIO as GPIO
from time import sleep
from semaforo import estados
from valores import TEMPO


QTD_ESTADOS = 6
botaoPedestrePrincipal = False
botaoPedestreAuxiliar = False


def trataBotaoPrincipal(channel):
        global botaoPedestrePrincipal
        botaoPedestrePrincipal = not botaoPedestrePrincipal

def trataBotaoAuxiliar(channel):
        global botaoPedestreAuxiliar
        botaoPedestreAuxiliar = not botaoPedestreAuxiliar

def atualizaEstado(estadoAtual):
        global botaoPedestrePrincipal
        global botaoPedestreAuxiliar

        if estadoAtual == 1:
                tempo_max = TEMPO['PRINCIPAL_VERDE_MAXIMO']
                tempo_atual = TEMPO['PRINCIPAL_VERDE_MINIMO']
                while tempo_atual < tempo_max and botaoPedestrePrincipal == False:
                        sleep(0.1)
                        tempo_atual = tempo_atual + 0.1
                
                if botaoPedestrePrincipal:
                        botaoPedestrePrincipal = False
                        return 3
                else:
                        (estadoAtual + 1) % QTD_ESTADOS

        elif estadoAtual == 4:
                tempo_max = TEMPO['AUXILIAR_VERDE_MAXIMO']
                tempo_atual = TEMPO['AUXILIAR_VERDE_MINIMO']
                while tempo_atual < tempo_max and botaoPedestreAuxiliar == False:
                        sleep(0.1)
                        tempo_atual = tempo_atual + 0.1
        
                if botaoPedestreAuxiliar:
                        botaoPedestreAuxiliar = False
                        return 0
                else:
                        (estadoAtual + 1) % QTD_ESTADOS

        return (estadoAtual + 1) % QTD_ESTADOS

def inicializaCruzamento(CRUZAMENTO):
        semaforoPrincipal = [CRUZAMENTO['SEMAFORO_2_VERDE'], CRUZAMENTO['SEMAFORO_2_AMARELO'], CRUZAMENTO['SEMAFORO_2_VERMELHO']]
        semaforoAuxiliar = [CRUZAMENTO['SEMAFORO_1_VERDE'], CRUZAMENTO['SEMAFORO_1_AMARELO'], CRUZAMENTO['SEMAFORO_1_VERMELHO']]

        estadoAtual = 0

        GPIO.setup(semaforoPrincipal, GPIO.OUT)
        GPIO.setup(semaforoAuxiliar, GPIO.OUT)

        GPIO.setup(CRUZAMENTO['BOTAO_PEDESTRE_2'], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(CRUZAMENTO['BOTAO_PEDESTRE_1'], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.add_event_detect(CRUZAMENTO['BOTAO_PEDESTRE_2'],GPIO.RISING,callback=trataBotaoPrincipal, bouncetime=300)
        GPIO.add_event_detect(CRUZAMENTO['BOTAO_PEDESTRE_1'],GPIO.RISING,callback=trataBotaoAuxiliar, bouncetime=300)

        while True:
                estados[estadoAtual](semaforoPrincipal, semaforoAuxiliar)
                estadoAtual = atualizaEstado(estadoAtual)

        

