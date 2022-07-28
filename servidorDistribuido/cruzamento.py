import RPi.GPIO as GPIO
from time import sleep
from semaforo import estados
from valores import TEMPO


QTD_ESTADOS = 6

botoesPedestrePrincipal = dict (
        C1=False,
        C2=False,
)

botoesPedestreAuxiliar = dict (
        C1=False,
        C2=False,
)

def trataBotao(channel, CRUZAMENTO):
        global botoesPedestrePrincipal
        global botoesPedestreAuxiliar

        if channel == CRUZAMENTO['BOTAO_PEDESTRE_2']:
                botoesPedestrePrincipal[CRUZAMENTO['TIPO']] = not botoesPedestrePrincipal[CRUZAMENTO['TIPO']]
        else:
                botoesPedestreAuxiliar[CRUZAMENTO['TIPO']] = not botoesPedestreAuxiliar[CRUZAMENTO['TIPO']]

def atualizaEstado(estadoAtual, CRUZAMENTO):
        global botoesPedestrePrincipal
        global botoesPedestreAuxiliar

        if estadoAtual == 1:
                tempo_max = TEMPO['PRINCIPAL_VERDE_MAXIMO']
                tempo_atual = TEMPO['PRINCIPAL_VERDE_MINIMO']
                while tempo_atual < tempo_max and botoesPedestrePrincipal[CRUZAMENTO['TIPO']] == False:
                        sleep(0.1)
                        tempo_atual = tempo_atual + 0.1
                
                if botoesPedestrePrincipal[CRUZAMENTO['TIPO']]:
                        botoesPedestrePrincipal[CRUZAMENTO['TIPO']] = False
                        return 3
                else:
                        (estadoAtual + 1) % QTD_ESTADOS

        elif estadoAtual == 4:
                tempo_max = TEMPO['AUXILIAR_VERDE_MAXIMO']
                tempo_atual = TEMPO['AUXILIAR_VERDE_MINIMO']
                while tempo_atual < tempo_max and botoesPedestreAuxiliar[CRUZAMENTO['TIPO']] == False:
                        sleep(0.1)
                        tempo_atual = tempo_atual + 0.1
        
                if botoesPedestreAuxiliar[CRUZAMENTO['TIPO']]:
                        botoesPedestreAuxiliar[CRUZAMENTO['TIPO']] = False
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

        GPIO.add_event_detect(CRUZAMENTO['BOTAO_PEDESTRE_2'],GPIO.RISING,callback=lambda x: trataBotao(CRUZAMENTO['BOTAO_PEDESTRE_2'],CRUZAMENTO), bouncetime=300)
        GPIO.add_event_detect(CRUZAMENTO['BOTAO_PEDESTRE_1'],GPIO.RISING,callback=lambda x: trataBotao(CRUZAMENTO['BOTAO_PEDESTRE_1'],CRUZAMENTO), bouncetime=300)

        while True:
                estados[estadoAtual](semaforoPrincipal, semaforoAuxiliar)
                estadoAtual = atualizaEstado(estadoAtual, CRUZAMENTO)


        

